from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from pathlib import Path

from ai_generator import AIGenerator
from database import get_db, LinkedInPost, ProfileData, GeneratedPost
from config import config

app = FastAPI(title="MSZ - AI Content Generator", version="2.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI
ai_generator = AIGenerator()

# Request Models
class AddTrainingDataRequest(BaseModel):
    posts: List[str]
    is_user_profile: bool = False  # True if these are YOUR posts

class GeneratePostRequest(BaseModel):
    topic: str
    format_type: str = "story"  # story, listicle, question, insight

class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[dict]] = []

# Routes
@app.get("/", response_class=HTMLResponse)
async def root():
    html_file = Path("templates/index.html")
    if html_file.exists():
        return html_file.read_text(encoding='utf-8')
    return {"message": "MSZ AI Content Generator", "version": "2.0.0"}

@app.get("/api")
async def api_info():
    return {
        "message": "MSZ AI Content Generator",
        "version": "2.0.0",
        "status": "ready"
    }

@app.post("/add-training-data")
async def add_training_data(request: AddTrainingDataRequest, db: Session = Depends(get_db)):
    """
    Add training data to the system
    - Training posts: Examples of viral posts to learn patterns from
    - User profile posts: YOUR posts to learn YOUR voice/tone
    """
    try:
        added_count = 0
        
        for post_text in request.posts:
            if len(post_text.strip()) > 50:
                db_post = LinkedInPost(
                    post_text=post_text.strip(),
                    post_type="user_profile" if request.is_user_profile else "training_example"
                )
                db.add(db_post)
                added_count += 1
        
        db.commit()
        
        training_count = db.query(LinkedInPost).filter(
            LinkedInPost.post_type == "training_example"
        ).count()
        
        user_count = db.query(LinkedInPost).filter(
            LinkedInPost.post_type == "user_profile"
        ).count()
        
        return {
            "success": True,
            "posts_added": added_count,
            "total_training_posts": training_count,
            "total_user_posts": user_count,
            "message": f"Added {added_count} {'user profile' if request.is_user_profile else 'training'} posts"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-post")
async def generate_post(request: GeneratePostRequest, db: Session = Depends(get_db)):
    """Generate a LinkedIn post on any topic"""
    try:
        # Get all posts for style analysis
        all_posts = db.query(LinkedInPost).all()
        
        if not all_posts:
            raise HTTPException(
                status_code=400, 
                detail="No training data found. Please add training posts first."
            )
        
        # Analyze writing style
        post_texts = [p.post_text for p in all_posts]
        style_guide = ai_generator.analyze_writing_style(post_texts)
        
        # Generate post
        result = ai_generator.generate_original_post(
            topic=request.topic,
            style_guide=style_guide,
            format_type=request.format_type
        )
        
        # Save to database
        generated_post = GeneratedPost(
            content=result['content'],
            source_type='original',
            hashtags=','.join(result['hashtags'])
        )
        db.add(generated_post)
        db.commit()
        
        return {
            "success": True,
            "post": result['content'],
            "hashtags": result['hashtags'],
            "style_learned_from": f"{len(all_posts)} posts"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-similar")
async def generate_similar(request: GeneratePostRequest, db: Session = Depends(get_db)):
    """Generate a post similar to the provided example"""
    try:
        # Get all posts for context
        all_posts = db.query(LinkedInPost).all()
        post_texts = [p.post_text for p in all_posts]
        style_guide = ai_generator.analyze_writing_style(post_texts)
        
        # Generate similar post
        result = ai_generator.generate_similar_post(
            example_post=request.topic,  # Using 'topic' field to pass the example post
            style_guide=style_guide
        )
        
        # Save to database
        generated_post = GeneratedPost(
            content=result['content'],
            source_type='similar',
            hashtags=','.join(result['hashtags'])
        )
        db.add(generated_post)
        db.commit()
        
        return {
            "success": True,
            "post": result['content'],
            "hashtags": result['hashtags'],
            "style_learned_from": f"{len(all_posts)} posts"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats")
async def get_stats(db: Session = Depends(get_db)):
    """Get training statistics"""
    training_posts = db.query(LinkedInPost).filter(
        LinkedInPost.post_type == "training_example"
    ).count()
    
    user_posts = db.query(LinkedInPost).filter(
        LinkedInPost.post_type == "user_profile"
    ).count()
    
    generated_posts = db.query(GeneratedPost).count()
    
    return {
        "training_posts": training_posts,
        "user_profile_posts": user_posts,
        "generated_posts": generated_posts,
        "total_learning_data": training_posts + user_posts
    }

@app.get("/generated-posts")
async def get_generated_posts(db: Session = Depends(get_db)):
    """View all generated posts"""
    posts = db.query(GeneratedPost).order_by(GeneratedPost.created_at.desc()).limit(20).all()
    
    return {
        "posts": [
            {
                "id": p.id,
                "content": p.content,
                "hashtags": p.hashtags.split(',') if p.hashtags else [],
                "created_at": p.created_at.isoformat()
            }
            for p in posts
        ]
    }

@app.get("/trending-ideas")
async def get_trending_ideas():
    """Get trending post ideas based on current market trends"""
    try:
        ideas = ai_generator.generate_trending_ideas()
        return {
            "success": True,
            "ideas": ideas
        }
    except Exception as e:
        return {
            "success": False,
            "ideas": [
                "AI transformation in Saudi Arabia",
                "Vision 2030 tech opportunities",
                "Defense innovation in the region",
                "Startup ecosystem growth",
                "Digital transformation strategies"
            ]
        }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting MSZ AI Content Generator...")
    print(f"📍 API: http://localhost:8000")
    print(f"📚 Docs: http://localhost:8000/docs")
    print("\n✅ Model trained with existing data")
    print("📝 Ready to add your profile data and generate content!")
    uvicorn.run(app, host="0.0.0.0", port=8000)

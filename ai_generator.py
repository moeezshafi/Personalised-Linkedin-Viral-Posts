from openai import OpenAI
from typing import List, Dict, Optional
from config import config

class AIGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        self.saudi_context = config.SAUDI_CONTEXT
    
    def analyze_writing_style(self, posts: List[str]) -> str:
        """Analyze writing style from historical posts"""
        if not posts:
            return "Professional, engaging, and informative"
        
        sample_posts = "\n\n---\n\n".join(posts[:10])  # Use first 10 posts
        
        prompt = f"""Analyze the writing style of these LinkedIn posts and provide a concise style guide:

{sample_posts}

Provide a brief style analysis covering:
1. Tone (formal/casual/mix)
2. Common themes
3. Sentence structure preferences
4. Use of emojis/formatting
5. Call-to-action patterns

Keep it under 150 words."""

        response = self.client.chat.completions.create(
            model=config.CHEAP_MODEL,
            messages=[
                {"role": "system", "content": "You are a writing style analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    def summarize_transcript(self, transcript: str) -> str:
        """Summarize video transcript into key points"""
        prompt = f"""Summarize this video transcript into 3-5 key takeaways. Focus on actionable insights and main ideas:

{transcript[:4000]}  # Limit to avoid token limits

Provide a concise summary with bullet points."""

        response = self.client.chat.completions.create(
            model=config.CHEAP_MODEL,
            messages=[
                {"role": "system", "content": "You are a content summarization expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    def generate_from_youtube(
        self, 
        transcript_summary: str, 
        style_guide: Optional[str] = None,
        video_url: str = ""
    ) -> Dict:
        """Generate LinkedIn post from YouTube video"""
        
        system_prompt = f"""You are an expert LinkedIn content creator specializing in the Saudi Arabian market.

{self.saudi_context}

Your task: Transform video content into engaging LinkedIn posts that:
- Start with a powerful hook (first line grabs attention)
- Are well-structured with 3-5 short paragraphs
- Include relevant insights for Saudi professionals
- End with a thought-provoking question or call-to-action
- Include 5-8 hashtags (mix of English and Arabic)
- Match the user's writing style if provided

Format:
[Hook - attention-grabbing first line]

[Body paragraphs - key insights]

[Call-to-action or question]

[Hashtags]"""

        if style_guide:
            system_prompt += f"\n\nUser's Writing Style:\n{style_guide}"
        
        user_prompt = f"""Create a LinkedIn post based on this video content:

{transcript_summary}

Video URL: {video_url}

Make it engaging, valuable, and optimized for Saudi Arabian professionals."""

        response = self.client.chat.completions.create(
            model=config.DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        
        content = response.choices[0].message.content
        
        # Extract hashtags
        hashtags = self._extract_hashtags(content)
        
        return {
            "content": content,
            "hashtags": hashtags,
            "source": "youtube",
            "source_url": video_url
        }
    
    def generate_original_post(
        self,
        topic: str,
        style_guide: Optional[str] = None,
        format_type: str = "story"  # story, listicle, question, insight
    ) -> Dict:
        """Generate original LinkedIn post on a topic"""
        
        system_prompt = f"""You write viral LinkedIn posts. Study these patterns from the training data:

PATTERN 1 - Data/Research Hook:
"I spent 6 hours analyzing 17.3M LinkedIn reactions.

Found something that will make you sick:

Your biggest potential connection commented on your post last week.

You never noticed.

Here's what I discovered from the data:
- Most founders have no idea WHO is actually engaging
- The average creator has 15+ high-value profiles commenting regularly
- Most never connect because they can't identify the gold from the noise"

PATTERN 2 - Comparison Story:
"I know two founders.
One works 100 hours/week.
One works 20.

The 20-hour founder makes more.

The 100-hour founder:
- Raised $50M
- Burns $1M/month
- Owns 5%

The 20-hour founder:
- Raised $0
- Profits $300K/month
- Owns 100%

I asked the 20-hour founder his secret."

PATTERN 3 - Contrarian Take:
"Your CTO just spent $3M on microservices.
I'm about to show you why they should be FIRED.

THE $3M ARCHITECTURE MASSACRE:

Ex-Netflix CTO joins a startup.
1,000 users. $5M Series A.

First move? Build 47 microservices."

KEY RULES:
1. NO EMOJIS - Pure text only
2. Short sentences - 1-2 lines max
3. Blank lines between paragraphs
4. Use "-" for bullet points
5. Build tension then reveal
6. End with question or statement
7. Add hashtags at the end

ADAPT TO SAAD'S CONTEXT:
- Saudi Arabia market
- AI/ML/Defense tech topics
- Vision 2030
- Startup ecosystem
- But NEVER say "As an AI engineer" or introduce yourself
- Just tell the story

Write EXACTLY like the training examples. Same rhythm. Same structure. Same punch."""

        if style_guide:
            system_prompt += f"\n\nAdditional style notes:\n{style_guide}"
        
        user_prompt = f"""Write a viral LinkedIn post about: {topic}

Use the EXACT format from training examples:
- Shocking hook (first line)
- Build tension
- Reveal insight
- Use bullets with "-"
- Short paragraphs
- No emojis
- End with impact

Topic context: Saudi Arabia, AI/tech, Vision 2030, startups

Write it now."""

        response = self.client.chat.completions.create(
            model=config.DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.85
        )
        
        content = response.choices[0].message.content
        hashtags = self._extract_hashtags(content)
        
        return {
            "content": content,
            "hashtags": hashtags,
            "source": "original",
            "topic": topic
        }
    
    def generate_similar_post(
        self,
        example_post: str,
        style_guide: Optional[str] = None
    ) -> Dict:
        """Generate a post on same topic but using trained viral structure"""
        
        system_prompt = f"""You write viral LinkedIn posts using the TRAINED STRUCTURE from these examples:

VIRAL STRUCTURE (from training):
"I spent 6 hours analyzing 17.3M LinkedIn reactions.

Found something that will make you sick:

Your biggest potential connection commented on your post last week.

You never noticed.

Here's what I discovered from the data:
- Most founders have no idea WHO is actually engaging
- The average creator has 15+ high-value profiles commenting regularly"

OR

"I know two founders.
One works 100 hours/week.
One works 20.

The 20-hour founder makes more.

The 100-hour founder:
- Raised $50M
- Burns $1M/month
- Owns 5%"

YOUR TASK:
1. Read the example post to understand the TOPIC only
2. Write about the SAME topic
3. But use the VIRAL STRUCTURE from training (short lines, bullets, hooks, reveals)
4. Different story, different examples, different data
5. NO EMOJIS - pure text
6. Adapt to Saudi Arabia context when relevant

CRITICAL: 
- Topic = from example post
- Structure/tone/voice = from training data (batches 1-4)
- Content = new and different

{self.saudi_context}"""

        if style_guide:
            system_prompt += f"\n\nTrained viral patterns:\n{style_guide}"
        
        user_prompt = f"""Example post (extract the TOPIC only):

{example_post}

Now write a post about the SAME topic but:
- Use VIRAL STRUCTURE from training (short punchy lines, bullets with "-", dramatic hooks)
- NO EMOJIS
- Different story/examples/data
- Keep the trained tone and voice
- Adapt to Saudi Arabia/regional context

Write it now using the viral format."""

        response = self.client.chat.completions.create(
            model=config.DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.85
        )
        
        content = response.choices[0].message.content
        hashtags = self._extract_hashtags(content)
        
        return {
            "content": content,
            "hashtags": hashtags,
            "source": "similar"
        }
    
    def generate_trending_ideas(self) -> List[str]:
        """Generate trending post ideas based on current topics"""
        
        prompt = """Generate 5 trending LinkedIn post ideas for Muhammad Saad Zaheer.

Context:
- AI/ML expert in Saudi Arabia
- Focus: Vision 2030, defense tech, fintech, startups
- Companies: Remote Stack AI, Falcon Sight, Nevox AI
- Audience: Saudi professionals, founders, tech leaders

Requirements:
- Topics should be timely and relevant
- Mix of: AI trends, Saudi market, startup insights, tech innovation
- Each idea should be specific and actionable
- Format: Just the topic, no numbering

Examples:
"AI adoption challenges in Saudi enterprises"
"Why Pakistani startups are moving to Riyadh"
"Defense tech opportunities in Vision 2030"

Generate 5 fresh ideas now (one per line, no numbers):"""

        response = self.client.chat.completions.create(
            model=config.CHEAP_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=200
        )
        
        content = response.choices[0].message.content.strip()
        ideas = [line.strip() for line in content.split('\n') if line.strip() and not line.strip()[0].isdigit()]
        
        # Fallback ideas if API fails
        if not ideas:
            ideas = [
                "AI transformation in Saudi Arabia",
                "Vision 2030 tech opportunities",
                "Defense innovation in the region",
                "Startup ecosystem growth in KSA",
                "Digital transformation strategies"
            ]
        
        return ideas[:5]
    
    def _extract_hashtags(self, content: str) -> List[str]:
        """Extract hashtags from generated content"""
        import re
        hashtags = re.findall(r'#\w+', content)
        return hashtags

# Test function
def test_ai_generator():
    generator = AIGenerator()
    
    # Test original post generation
    result = generator.generate_original_post(
        topic="The future of AI in Saudi Arabia",
        format_type="insight"
    )
    
    print("📝 Generated Post:")
    print(result['content'])
    print(f"\n🏷️ Hashtags: {', '.join(result['hashtags'])}")

if __name__ == "__main__":
    test_ai_generator()

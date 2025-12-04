from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import config

Base = declarative_base()

class LinkedInPost(Base):
    __tablename__ = "linkedin_posts"
    
    id = Column(Integer, primary_key=True, index=True)
    post_text = Column(Text, nullable=False)
    post_date = Column(String, nullable=True)
    engagement_count = Column(Integer, default=0)
    post_type = Column(String, nullable=True)  # text, image, video, carousel
    scraped_at = Column(DateTime, default=datetime.utcnow)

class ProfileData(Base):
    __tablename__ = "profile_data"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    headline = Column(String, nullable=True)
    about = Column(Text, nullable=True)
    current_position = Column(String, nullable=True)
    location = Column(String, nullable=True)
    scraped_at = Column(DateTime, default=datetime.utcnow)

class GeneratedPost(Base):
    __tablename__ = "generated_posts"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    source_type = Column(String, nullable=False)  # youtube, original, repurpose
    source_url = Column(String, nullable=True)
    hashtags = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    used = Column(Boolean, default=False)

# Create engine and tables
engine = create_engine(config.DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

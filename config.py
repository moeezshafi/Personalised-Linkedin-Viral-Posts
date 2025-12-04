import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # LinkedIn
    LINKEDIN_PROFILE_URL = os.getenv("LINKEDIN_PROFILE_URL")
    
    # Target Audience
    TARGET_AUDIENCE = os.getenv("TARGET_AUDIENCE", "saudi_arabia")
    
    # Database
    DATABASE_URL = "sqlite:///./msz_data.db"
    
    # Scraping Settings
    SCRAPE_DELAY_MIN = 2  # seconds
    SCRAPE_DELAY_MAX = 5  # seconds
    MAX_POSTS_TO_SCRAPE = 100
    
    # AI Settings
    DEFAULT_MODEL = "gpt-4-turbo-preview"
    CHEAP_MODEL = "gpt-3.5-turbo"
    
    # Saudi Audience Context
    SAUDI_CONTEXT = """
    Target Audience: Saudi Arabian professionals
    Cultural Considerations:
    - Professional yet warm and relationship-focused
    - Reference Vision 2030 and regional business trends
    - Mix English professional terms with cultural context
    - Include both English and Arabic hashtags
    - Respect Gulf business etiquette
    Popular Topics: Digital transformation, entrepreneurship, innovation, tech, Vision 2030
    """

config = Config()

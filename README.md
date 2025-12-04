# Personalized LinkedIn Viral Posts Generator

AI-powered LinkedIn content generator that creates viral posts using your voice and proven engagement patterns.

## Features

- 🚀 **Viral Post Generation** - Creates engaging LinkedIn posts using proven viral patterns
- 🎯 **Personalized Voice** - Learns from your writing style and tone
- 💡 **Trending Ideas** - AI-generated post ideas based on current trends
- 🇸🇦 **Saudi Arabia Focus** - Optimized for Saudi professionals and Vision 2030
- ⚡ **Two Generation Modes**:
  - Topic-based: Enter any topic
  - Example-based: Paste any post to generate similar content

## Tech Stack

- **Backend**: FastAPI (Python)
- **AI**: OpenAI GPT-4 & GPT-3.5
- **Database**: SQLite with SQLAlchemy
- **Frontend**: HTML, TailwindCSS, Vanilla JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/moeezshafi/Personalised-Linkedin-Viral-Posts.git
cd Personalised-Linkedin-Viral-Posts
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

4. Train the model:
```bash
python complete_training.py
```

5. Start the server:
```bash
python main.py
```

6. Open browser:
```
http://localhost:8000
```

## Quick Start (Windows)

```bash
install.bat
start.bat
```

## How It Works

1. **Training Data**: The AI is trained on:
   - 19 viral LinkedIn posts (proven engagement patterns)
   - Your personal posts (your voice and tone)
   - Total: 31 posts for comprehensive learning

2. **Generation**: 
   - Combines viral hooks and structures
   - Maintains your authentic voice
   - Adapts to Saudi Arabia context
   - No emojis, pure text format

3. **Trending Ideas**:
   - AI analyzes current market trends
   - Generates personalized topic suggestions
   - One-click generation

## Project Structure

```
├── main.py                 # FastAPI server
├── ai_generator.py         # AI content generation logic
├── database.py             # Database models
├── config.py               # Configuration
├── train_model.py          # Training script
├── complete_training.py    # Complete training setup
├── templates/
│   └── index.html         # Web interface
├── requirements.txt        # Python dependencies
└── .env                   # API keys (create this)
```

## API Endpoints

- `GET /` - Web interface
- `POST /generate-post` - Generate post from topic
- `POST /generate-similar` - Generate similar post from example
- `GET /trending-ideas` - Get AI-generated trending ideas
- `GET /stats` - View training statistics

## Training Your Own Voice

1. Add your LinkedIn posts to `add_saad_profile.py`
2. Run: `python add_saad_profile.py`
3. The AI will learn your writing style

## Customization

Edit `config.py` to customize:
- Target audience
- AI models
- Saudi Arabia context
- Generation parameters

## License

MIT License

## Author

Moeez Shafi
- GitHub: [@moeezshafi](https://github.com/moeezshafi)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/moeezshafi)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

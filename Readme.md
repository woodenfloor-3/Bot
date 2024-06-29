# Telegram Bot with SauceNAO Image Search

This Telegram bot allows users to perform reverse image searches using SauceNAO API.

## Installation and Setup

```bash
# Clone repository and navigate to project directory
git clone <repository-url>
cd <repository-name>

# Set up virtual environment (optional but recommended)
python -m venv env
source env/bin/activate  # Windows: `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Configure API keys
config.py

echo 'BOT_TOKEN = "<your-telegram-bot-token>"\nSAUCENAO_API_KEY = "<your-saucenao-api-key>"' > 

# Run the bot
python bot.py

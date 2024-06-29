# Telegram Bot with SauceNAO Image Search

This Telegram bot allows users to perform reverse image searches using SauceNAO API.

## Installation and Setup

## Clone repository and navigate to project directory
```bash
git clone https://github.com/woodenfloor-3/Bot.git
cd Bot
```
## Set up virtual environment (optional but recommended)
```bash
python -m venv env
source env/bin/activate 
``` 
## Windows: 
```bash
env\Scripts\activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Configure API keys 
config.py
```bash
echo 'BOT_TOKEN = "<your-telegram-bot-token>"
SAUCENAO_API_KEY = "<your-saucenao-api-key>"' 
```
## Run the bot
```bash
python bot.py
```

## Contributing
Feel free to contribute to this project. Fork and create a pull request with your changes.

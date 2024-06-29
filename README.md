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

## LICENSE
MIT License

Copyright (c) 2024 woodenfloor-3

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

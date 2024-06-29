import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext
from telegram.constants import ParseMode
from telegram.ext import filters
from config import SAUCENAO_API_KEY,BOT_TOKEN


# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Function to perform SauceNAO search
def perform_search(api_url, api_key, image_data):
    data = {
        'output_type': 2,   # JSON API
        'api_key': api_key,
        'testmode': 1,      # Testing mode
        'numres': 1,        # Number of results requested
        'db': 999           # Search all databases
    }
    files = {'file': image_data}

    response = requests.post(api_url, data=data, files=files)
    response.raise_for_status()  

    return response.json() 

# Start command handler
async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}!\n"
        "I can help you find similar images using SauceNAO. Send me a photo and I'll search the web for visually similar ones.\n"
        "Note: Using SauceNAO may be subject to usage limits or costs. Please refer to their documentation for details."
    )

# Reverse image search handler
async def reverse_image_search(update: Update, context: CallbackContext):
    photo = update.message.photo[-1]  # Get the largest photo size

    # Download the photo
    file = await context.bot.get_file(photo.file_id)
    file_url = file.file_path
    image_data = requests.get(file_url).content

    # Perform search using SauceNAO API
    saucenao_results = perform_search(SAUCENAO_API_URL, SAUCENAO_API_KEY, image_data)

    # Prepare response message
    response_text = "Search Results:\n\n"

    # Process SauceNAO results
     # Process SauceNAO results
    if saucenao_results and 'results' in saucenao_results:
        results = saucenao_results['results'][:4]  # Limit to the first 4 results
        keyboard = []
        for index, result in enumerate(results, start=1):
            result_data = result.get('data', {})
            ext_urls = result_data.get('ext_urls', [])
            if ext_urls:
                image_url = ext_urls[0]
                site_name = get_site_name(image_url)
                button_text = f"Result {index} ({site_name})"
                keyboard.append([InlineKeyboardButton(button_text, url=image_url)])
                response_text += f"{index}. [{button_text}]({image_url})\n"

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(response_text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)
    else:
        response_text += "SauceNAO: No similar images found."
        await update.message.reply_text(response_text)


def get_site_name(url):
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain.split('.')[0].capitalize()


# Help command handler
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Send me a photo and I'll search for similar images using SauceNAO."
    )

# Error handler
async def error_handler(update: Update, context: CallbackContext):
    error = context.error
    logging.error(f"An error occurred: {error}")

    if isinstance(error, (requests.exceptions.RequestException, ValueError)):
        await update.message.reply_text(
            "An error occurred during the search. Please try again later."
        )

# Main function to start the bot
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, reverse_image_search))
    application.add_error_handler(error_handler)

    # Start the Bot
    application.run_polling()

if __name__ == "__main__":
    main()

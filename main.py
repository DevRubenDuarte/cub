import os, logging
from dotenv import load_dotenv
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, ContextTypes
from commands import command_populator

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Set up Telegram bot token - EXPECTS .env file with TELEGRAM_BOT_TOKEN="xxxxx"
token = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    # Create Application and pass bot token
    application = ApplicationBuilder().token(token).build()

    # Register start command handler
    command_populator(application)

    # Start the Bot
    application.run_polling()

if __name__ == "__main__":
    main()



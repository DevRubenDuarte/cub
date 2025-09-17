from telegram import Update, ForceReply
from telegram.ext import ContextTypes, CommandHandler

# Populate commands into the application - Add command here, define it below
def command_populator(application):
    application.add_handler(CommandHandler("start", start))

# Define command here
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Welcome to the bot.",
        reply_markup=ForceReply(selective=True),
    )



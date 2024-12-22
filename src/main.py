import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import Config


def init_logger() -> logging.Logger:
    """
    Initializes the logger with a specific format and level.
    Returns:
        logging.Logger: Configured logger instance.
    """
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,)
    return logging.getLogger(__name__)

def log_session(update: Update, response_message: str) -> None:
    """
    Logs the session details including the received command and response message.
    Args:
        update (Update): The update object containing the message details.
        response_message (str): The response message to be logged.
    """
    logger.info(f"Received \"{update.effective_message.text}\" command from user \"{update.effective_user.username}\" in \"{update.effective_chat.type}\" chat.")
    logger.info(f"Chat ID: \"{update.effective_chat.id}\", User ID: \"{update.effective_user.id}\"")
    logger.info(f"Response message: \"{response_message}\"")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command. Sends a welcome message to the user.
    Args:
        update (Update): The update object containing the message details.
        context (ContextTypes.DEFAULT_TYPE): The context object for the command.
    """
    welcome_message = f"Hello {update.effective_user.first_name}! I'm a bot, {config.bot_name}! 🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️ \n"
    log_session(update, welcome_message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /help command. Sends a help message to the user.
    Args:
        update (Update): The update object containing the message details.
        context (ContextTypes.DEFAULT_TYPE): The context object for the command.
    """
    help_message = f"Hello {update.effective_user.first_name}! I'm a bot, {config.bot_name}! 🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️ \nTo start using me send me /start"
    log_session(update, help_message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /caps command. Converts the provided text to uppercase and sends it back to the user.
    Args:
        update (Update): The update object containing the message details.
        context (ContextTypes.DEFAULT_TYPE): The context object for the command.
    """
    text_caps = " ".join(context.args).upper() if context.args else "Usage: /caps <some text>"
    log_session(update, text_caps)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def main() -> None:
    """
    Main entry point of the bot application. Initializes the logger, loads environment variables,
    and sets up command handlers for the bot.
    """
    global logger, config
    logger = init_logger()
    config = Config()

    application = ApplicationBuilder().token(config.bot_token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('caps', caps))

    application.run_polling()

if __name__ == '__main__':
    main()

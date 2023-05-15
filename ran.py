
import random
import string
import telegram
from telegram.ext import Updater, CommandHandler

# Define the bot token and create an instance of the bot
TOKEN = '6138107355:AAGuP7Rtf36n8NQGNwPehnn5ClTGBtZeEeQ'
bot = telegram.Bot(token=TOKEN)

# Define the command for generating a random password
def generate_password(update, context):
    # Generate a random password using uppercase and lowercase letters, digits, and symbols
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
    
    # Send the generated password to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your new password is: {password}")

# Create an instance of the Updater class and attach the command handler
updater = Updater(token=TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('generate_password', generate_password))

# Start the bot
updater.start_polling()
updater.idle()

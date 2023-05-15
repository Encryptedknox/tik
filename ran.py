import telebot
import string
import random
from random import choice

# Create an instance of the TeleBot class
bot = telebot.TeleBot("6138107355:AAGuP7Rtf36n8NQGNwPehnn5ClTGBtZeEeQ")

# Define a message handler that handles incoming /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello, {message.chat.username}")

# Define another message handler that handles /generate_password command
@bot.message_handler(commands=['gen'])
def generate_password(message):
    # Generate a random password
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for _ in range(random.randint(8, 16)))

    # Send the password to the user
    bot.send_message(message.chat.id, f"Generated password: {password}")

# Run the bot
bot.polling()

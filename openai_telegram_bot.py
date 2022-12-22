import openai
import telegram
from telegram.ext import Updater, MessageHandler
from telegram.bot import Bot
import os
from dotenv import load_dotenv

load_dotenv(".env")

def get_openai_response(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"This is a conversation with an AI assistant. The assistant is helpful, creative, clever and friendly.\nHuman: Hello, can you help me?\nAI: Of course! How may I help you?\nHuman: {message}\nAI: ",
        temperature=0.9,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
)

    # Return the response generated by openai
    return(response["choices"][0]["text"])

def send_telegram_message(chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)

def handle_telegram_message(update, context):
    # Verify that the update is a message and has the required attributes
    if isinstance(update.message, telegram.Message) and update.message.chat_id and update.message.text:
        # Get the chat ID and message from the update
        chat_id = update.message.chat_id
        text = update.message.text
        
        # Get the response from openai
        response = get_openai_response(text)
        
        # Send the response back to the user
        send_telegram_message(chat_id, response)

if __name__ == "__main__":
    # Replace <YOUR_API_TOKEN> with your openai API token
    openai.api_key = os.getenv["OPENAI_KEY"]
    
    # Replace <YOUR_TELEGRAM_BOT_TOKEN> with your Telegram bot's token
    bot = Bot(token = os.getenv["TELEGRAM_KEY"])
    
    # Create an updater object to handle updates
    updater = Updater(bot=bot, request_kwargs={'pool_size': 8})
    
    # Create a message handler that will call the `handle_message` function
    # whenever a new message is received
    message_handler = MessageHandler(filters=None, callback=handle_telegram_message)

    # Tell the updater to use the message handler
    updater.dispatcher.add_handler(message_handler)
    
    # Start the updater, which will listen for new messages and call
    # the `handle_telegram_message` function when a new message is received
    updater.start_polling()
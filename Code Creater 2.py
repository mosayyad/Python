#Code Written By Mohammed-Sayyad
#Code Start:

name=input("Your Name: " ).upper()

complete="""
Complteted Your Prosses
Check Your Path
if you don't Your Path 
Check Programme path 
where created File
"""

Files_available="Hello"+name+"""
YOur Files available:
1-ChatGPT
2-Telegram Bot 
if You get erro after run any file from creater check spaces in file
"""
print(Files_available)

input=input("What's Your File Would You Create:  " ).lower()


if input == "chatgpt":
    chatgpt=open("ChatGPT.py","w")
    chatgpt.write("""
import openai

# Set up your OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,  # Adjust the number of tokens based on your desired response length
        temperature=0.7,  # Adjust the temperature to control the randomness of the response
        n = 1,
        stop=None,
        timeout=None
    )

    # Extract the generated response
    generated_text = response.choices[0].text.strip()

    return generated_text

def chat():
    print("Welcome to the chatbot. Enter 'quit' to exit.")

    while True:
        # Get user input
        user_input = input("User: ")

        # Check if user wants to quit
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Generate a response
        prompt = "User: " + user_input + "\nBot:"
        response = generate_response(prompt)
        
        # Print the response
        print("Bot: " + response)

# Run the chat function
chat()

""")
    print(complete)
elif input == "telegram bot":
    telegram_bot=open("TelegrameBot.py","w")
    telegram_bot.write("""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Replace 'YOUR_BOT_TOKEN' with the token obtained from BotFather
bot_token = 'YOUR_BOT_TOKEN'

# Create an instance of the Updater class
updater = Updater(token=bot_token, use_context=True)
# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Telegram bot.")

# Create a CommandHandler for the /start command
start_handler = CommandHandler('start', start)

# Register the CommandHandler with the updater
updater.dispatcher.add_handler(start_handler)

# Define a function to handle regular text messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Create a MessageHandler for regular text messages
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

# Register the MessageHandler with the updater
updater.dispatcher.add_handler(echo_handler)
# Start the bot
updater.start_polling()

# Keep the script running until it is interrupted
updater.idle()

""")
    print(complete)
else:
    print("Input Err")
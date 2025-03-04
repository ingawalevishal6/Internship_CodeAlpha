"""Code writen by vishal ingawale"""
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pair= [
    [
        r"hi|hello|hey",
        [" Hello!","Hi! How can I help you?"]
    ],
    [
        r"how are you?",
        [" I'm just a bot, but I'm doing well! How about you?"]
    ],
    [
        r"(.*) your name?",
        [" I'm a chatbot created to assist you. You can call me ChatBot!"]
    ],
    [
        r"what can you do?",
        ["  I can chat with you, answer basic questions, and keep you entertained!"]
    ],
    [
        r"bye|goodbye",
        [" Goodbye! Have a great day!", "Bye! Take care!"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pair, reflections)

def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to exits.")
    while True:
        user_input = input(": ")
        if user_input.lower() == "bye":
            print("Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    start_chat()

import pywhatkit
from colorama import Fore, Back, Style, init
import random

# Initialize colorama to autoreset, ensuring each print resets after use
init(autoreset=True)

# Responses for different topics
greetings = [
    "Hello there! How can I help you today?",
    "Hey! It's great to chat with you.",
    "Hi! What's on your mind?"
]

farewells = [
    "Goodbye! Talk to you later.",
    "See you next time!",
    "It was nice chatting with you. Bye for now!"
]

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the computer so cold? Because it left its Windows open!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "What do you call a fake noodle? An impasta!",
    "Why did the bicycle fall over? Because it was two tired!"
]

# Helper function to normalize user input
def normalize_input(text):
    return text.strip().lower()

# Function to handle greetings
def greet():
    print(Fore.CYAN + f"ChatBot: {random.choice(greetings)}")

# Function to tell a joke
def tell_joke():
    joke = random.choice(jokes)
    print(Fore.MAGENTA + f"ChatBot: {joke}")

# Function to play a song using pywhatkit
def play_song(song_name):
    try:
        print(Fore.GREEN + f"ChatBot: Playing '{song_name}' on YouTube now!")
        pywhatkit.playonyt(song_name)
    except Exception as e:
        print(Fore.RED + f"ChatBot: Sorry, I couldn't play that song. Error: {e}")

# Main chat function to interact with the user
def chat():
    greet()
    while True:
        user_input = normalize_input(input(Fore.CYAN + "You: "))

        if "joke" in user_input:
            tell_joke()
        elif "song" in user_input:
            print(Fore.YELLOW + "ChatBot: What song would you like to hear? Please enter the name of the song.")
            song_input = input(Fore.YELLOW + "You: ")
            print(Fore.GREEN + f"ChatBot: '{song_input}', what a great choice! 🎶")
            play_song(song_input)
        elif user_input == "exit" or user_input == "goodbye" or user_input == "bye":
            print(Fore.CYAN + f"ChatBot: {random.choice(farewells)}")
            break
        else:
            print(Fore.RED + "ChatBot: I'm sorry, I don't understand that command. You can ask me to 'tell a joke' or 'play a song'. You can also say 'exit' to end our chat.")

if __name__ == "__main__":
    chat()
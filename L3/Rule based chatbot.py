# Lesson Name : Building Rule based Chatbots
# Activity-1 Name : Rule based Chatbot

#------------------------------------------------------------------------------------------------------------------------------------


from colorama import Fore, Back, Style, init
import random

init(autoreset=True)
# Initialize colorama to autoreset, ensuring each print resets after use

destinations = {
    "Maldives": "beaches",
    "Switzerland": "mountains",
    "Paris": "city",
    "Tokyo": "city",
    "Nepal": "mountains",
    "New York": "city",
    "London": "city",
    "Thailand": "beaches",
    "Hawaii": "beaches",
    "Rome": "city"
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why was the computer so cold? Because it left its Windows open!",
    "I told my computer I needed a break, and now it's sending me coffee pictures.",
    "What do you call a computer that sings? A Dell!"
]

# Helper function to normalize user input by removing extra spaces, and lowering case
def normalize_input(text):
    return text.strip().lower()

# Function to get a travel recommendation based on user's input
def recommend(user_input):
    for destination, type in destinations.items():
        if user_input in type:
            print(Fore.GREEN + f"TravelBot: {destination} is a great choice!")
            return
    print(Fore.RED + "TravelBot: Sorry, I don't have a destination for that type of trip.")

# Function to give packing tips based on user's destination
def packing_tips(destination):
    print(Fore.CYAN + f"TravelBot: Packing tips for {destination}:")
    print(Fore.GREEN + "  - Bring chargers and adapters")
    print(Fore.YELLOW + "  - Pack comfortable shoes")
    print(Fore.BLUE + "  - Check the local weather before you go")

# Function to tell a joke
def tell_joke():
    joke = random.choice(jokes)
    print(Fore.MAGENTA + f"TravelBot: {joke}")

# Main chat function to interact with the user
def chat():
    print(Fore.CYAN + "Hello, I'm TravelBot!")
    while True:
        user_input = normalize_input(input(Fore.CYAN + "You: "))

        if user_input == "recommend":
            print(Fore.YELLOW + "TravelBot: What kind of trip are you looking for? (e.g., beaches, mountains, or cities)")
            recommend_input = normalize_input(input(Fore.YELLOW + "You: "))
            recommend(recommend_input)
        elif user_input == "packing tips":
            print(Fore.YELLOW + "TravelBot: What's your destination? (e.g., Paris, Maldives)")
            destination_input = normalize_input(input(Fore.YELLOW + "You: "))
            if destination_input.capitalize() in destinations:
                packing_tips(destination_input.capitalize())
            else:
                print(Fore.RED + "TravelBot: Sorry, I don't have packing tips for that destination yet.")
        elif user_input == "tell a joke":
            tell_joke()
        elif user_input == "exit" or user_input == "goodbye":
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: I'm sorry, I don't understand that command. You can try 'recommend', 'packing tips', 'tell a joke', or 'exit'.")

if __name__ == "__main__":
    chat()
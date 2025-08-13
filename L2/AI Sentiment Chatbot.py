# Lesson Name : How AI Works: From Data to Smart Models
# Activity-1 Name : Sentiment Spy

#------------------------------------------------------------------------------------------------------------------------------------







# Import colorama
import colorama
from colorama import Fore, Style
from textblob import TextBlob
# Initialize colorama for colored output
colorama.init()
# Instructions for the start of the program
print(f"{Fore.CYAN}👋 Welcome to Sentiment Spy!🕵️‍♂️{Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent" # Fallback if user doesn't provide a name
# Store conversation and a list of tuples: (text, polarity, sentiment_type)
conversation_history = []
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!👋")
print(f"{Fore.CYAN}I am Sentiment Spy and I will analyze your sentences with TextBlob and show you the sentiment.🧐")
print(f"{Fore.CYAN}Type:{Fore.GREEN}'exit'{Fore.CYAN} to end our conversation. (e.g. {Fore.CYAN}exit){Fore.CYAN}")
print(f"{Fore.YELLOW}Type:{Fore.YELLOW}'quit'{Fore.CYAN} to end our conversation. (e.g. {Fore.CYAN}quit){Fore.CYAN}")
while True:
    user_input = input(f"{Fore.GREEN}>>>{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue
    # Check for commands
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE}👋 Exiting Sentiment Spy. Farewell, Agent {user_name}!👋{Style.RESET_ALL}")
        break
    elif user_input.lower() == "clear":
        conversation_history.clear()
        print(f"{Fore.CYAN}✅ All conversation history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for i, (text, _, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😄"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😠"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{i}. {color}{emoji}{text}{Style.RESET_ALL} (Polarity: {polarity:.2f}, {sentiment_type})")
        continue
    # Analyze sentiment
    textblob = TextBlob(user_input)
    polarity = textblob.sentiment.polarity
    if polarity > 0:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😄"
    elif polarity < 0:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😠"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"
    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))
    # Print result with color, emoji, and polarity
    print(f"{color}{emoji}{sentiment_type} sentiment detected!👀{Style.RESET_ALL}")
    print(f"Polarity: {polarity:.2f}{Style.RESET_ALL}")
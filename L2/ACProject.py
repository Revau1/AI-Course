import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize Colorama for cross-platform color support
colorama.init(autoreset=True)

print(f"{Fore.CYAN}👋 Welcome to Sentiment Spy!🕵️‍♂️")
user_name = input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Unknown User"

conversation_history = []
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!👋")
print(f"{Fore.CYAN}I am Sentiment Spy and I will analyze your sentences with TextBlob and show you the sentiment.🧐")
print(f"{Fore.CYAN}Type '{Fore.GREEN}exit'{Fore.CYAN} or '{Fore.GREEN}quit'{Fore.CYAN} to end our conversation.")
print(f"{Fore.CYAN}Type '{Fore.YELLOW}history'{Fore.CYAN} to view your conversation history.")
print(f"{Fore.CYAN}Type '{Fore.RED}clear'{Fore.CYAN} to clear the history.")
print(f"{Fore.CYAN}Type '{Fore.BLUE}stats'{Fore.CYAN} to view sentiment statistics.")


while True:
    user_input = input(f"{Fore.GREEN}>>>{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Command Handling
    if user_input.lower() in ["exit", "quit"]:
        # Final Report on Exit
        print(f"\n{Fore.BLUE}👋 Exiting Sentiment Spy. Farewell, Agent {user_name}!👋")
        
        if conversation_history:
            positive_count = sum(1 for _, _, sentiment in conversation_history if sentiment == "Positive")
            negative_count = sum(1 for _, _, sentiment in conversation_history if sentiment == "Negative")
            neutral_count = sum(1 for _, _, sentiment in conversation_history if sentiment == "Neutral")
            total_entries = len(conversation_history)

            print(f"\n{Fore.CYAN}📈 Final Sentiment Report:{Style.RESET_ALL}")
            print(f"Total Sentences Analyzed: {total_entries}")
            print(f"{Fore.GREEN}Positive: {positive_count}{Style.RESET_ALL}")
            print(f"{Fore.RED}Negative: {negative_count}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Neutral: {neutral_count}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No conversation history to report.{Style.RESET_ALL}")

        break  # Exit the loop

    elif user_input.lower() == "stats":
        positive_count = sum(1 for _, _, sentiment in conversation_history if sentiment == "Positive")
        negative_count = sum(1 for _, _, sentiment in conversation_history if sentiment == "Negative")
        neutral_count = sum(1 for _, _, sentiment in conversation_history if sentiment == "Neutral")
        total_entries = len(conversation_history)

        if total_entries == 0:
            print(f"{Fore.YELLOW}No data to analyze yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📊 Sentiment Statistics:{Style.RESET_ALL}")
            print(f"Positive: {positive_count}")
            print(f"Negative: {negative_count}")
            print(f"Neutral: {neutral_count}")
            print(f"Total entries: {total_entries}")
        continue

    elif user_input.lower() == "clear":
        conversation_history.clear()
        print(f"{Fore.CYAN}✅ All conversation history cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for i, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😄"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😠"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{i}. {color}{emoji} {text}{Style.RESET_ALL} (Polarity: {polarity:.2f}, {sentiment_type})")
        continue

    # Sentiment Analysis
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

    # Store analysis and print result
    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}{emoji} {sentiment_type} sentiment detected!👀{Style.RESET_ALL}")
    print(f"Polarity: {polarity:.2f}{Style.RESET_ALL}")
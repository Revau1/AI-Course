# Greet the user
print("Hello! I am AI Bot. What's your name? : ")

# Get user input for name
name = input()

# Respond to the user's name
print(f"Nice to meet you, {name}!")

# Ask about the weather
print("How are you feeling the weather today? (e.g., sunny, rainy, cloudy): ")
weather_feeling = input().lower()
print(f"I see. It's interesting how different weather can make us feel.")

# Ask a question about their feelings
print("How are you feeling today? (good/bad) : ")
mood = input().lower()

# Use conditional statements to respond based on mood
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

# Ask for a favorite color
print("What is your favorite color? ")
favorite_color = input()
print(f"{favorite_color} is a wonderful color!")

# End the conversation
print(f"It was nice chatting with you {name}. Goodbye!")
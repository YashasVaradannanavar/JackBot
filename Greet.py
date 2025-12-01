import datetime

def get_greeting():
    now = datetime.datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        return "Good morning! ☀️"
    elif 12 <= hour < 17:
        return "Good afternoon! 🌤️"
    elif 17 <= hour < 21:
        return "Good evening! 🌆"
    else:
        return "Good night! 🌙 Hope you're doing well."

print("🤖 Greeting Bot (type 'exit' to quit)\n")

while True:
    user = input("You: ")
    if user.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye 👋")
        break

    greeting = get_greeting()
    print("Bot:", greeting, "\n")

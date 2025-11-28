import subprocess
#subprocess better and quicker
def ask_ollama(text):
    #Send text to Ollama(Phi3) version and return result
    result = subprocess.run(["ollama", "run", "phi3"], input=text,capture_output=True, text=True,encoding="utf-8",errors="ignore")
    return result.stdout.strip()

def greet_bot():
    print("\n******  Smart Greeting Bot using (phi3)  ******")

    hour = int(input("Enter hour (0–23): "))
    if hour < 12:
        base = "morning"
    elif hour < 17:
        base = "afternoon"
    elif hour < 20:
        base = "evening"
    elif hour < 23:
        base = "night"
    else:
        print("Invalid time given ")

    # Beautify with certain conditions
    prompt = (
        f"Write a SHORT greeting (max 7–10 words). "
        f"Make it friendly but brief with no questions. Clearly mention '{base}'. "
        f"Base greeting: Good {base}."
    )
    final_greeting = ask_ollama(prompt)

    print("\nBot:", final_greeting)

##run case
greet_bot()
condition=input("Do you want a greeting ? :")
while condition.lower() in ["yes","y"]:
    greet_bot()
    condition=input("Do you want another greeting ? :")


import datetime
import re
import math

def get_time():
    now = datetime.datetime.now()
    return now.strftime("The current time is %H:%M.")

def get_date():
    today = datetime.date.today()
    return today.strftime("Today's date is %B %d, %Y.")

def calculate(expression):
    # For simple math questions
    try:
        result = eval(expression)
        return f"The answer is {result}."
    except:
        return "Sorry, I can't calculate that."

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greeting
    greetings = ['hello', 'hi', 'hey']
    if any(greet in user_input for greet in greetings):
        return "Hello! How can I help you today?"
    # Gratitude
    if "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."
    # Apology
    if "sorry" in user_input:
        return "No problem! How can I assist you further?"
    # Compliment
    if "good bot" in user_input or "nice bot" in user_input:
        return "Thank you! I'm here to help you."
    # Affirmation
    if "yes" in user_input or "sure" in user_input:
        return "Great! What would you like to know?"
    # Negation
    if "no" in user_input or "not really" in user_input:    
        return "Okay, if you change your mind, feel free to ask me anything."
    # Farewell
    farewells = ['bye', 'goodbye', 'see you']
    if any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a nice day."

    # Ask for name
    if "your name" in user_input or "who are you" in user_input:
        return "I am a simple rule-based chatbot created in Python."
    # Ask for Developer Name
    if "developer" in user_input or "creator" in user_input:
        return "I was created by a Python enthusiast Mr.Bhatt Jaymeen a.k.a ethical-knight."
    #ask for Purpose
    if "purpose" in user_input or "what can you do" in user_input:
        return "I can tell you the current time, date, do simple math, developer name ,and answer basic questions."

    # Current time
    if "time" in user_input:
        return get_time()

    # Current date
    if "date" in user_input:
        return get_date()

    # Simple math
    match = re.search(r'(\d+ [\+\-\*/] \d+)', user_input)
    if match:
        expression = match.group(1)
        return calculate(expression)
    
    # Age question
    if "your age" in user_input or "how old" in user_input:
        return "I'm as old as the code that runs me!"

    # Weather (basic, static answer)
    if "weather" in user_input:
        return "I can't check live weather, but I hope it's nice where you are!"

    # Default fallback
    return "Sorry, I don't understand that. You can ask me about time, date, simple math, etc."

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
    if user_input.lower() in ['bye', 'goodbye', 'exit']:
        break

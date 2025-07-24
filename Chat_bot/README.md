# Simple Rule-Based Chatbot

A beginner-friendly, rule-based chatbot built in Python. This chatbot can respond to simple greetings, farewells, time, date queries, basic math calculations, and a few other predefined questions.

## Features

- Responds to greetings like "hello", "hi", "hey".
- Provides the current time and date.
- Performs simple math calculations (addition, subtraction, multiplication, division).
- Answers basic questions like "What's your name?" and "How old are you?"
- Gives polite responses for unknown queries.
- Easy to understand and extend for beginners.

## How It Works

- The chatbot listens for user input in a loop.
- It uses keyword matching and regular expressions to detect user intents.
- It replies based on predefined rules inside the `chatbot_response` function.
- If the input contains a math expression (e.g., "2 + 3"), it evaluates and returns the result.
- Unrecognized questions receive a default friendly response.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Running the Chatbot

1. Clone or download the project files.
2. Open a terminal/command prompt in the project directory.
3. Run the chatbot script using:

python chatbot.py

text

4. Start chatting! Type 'bye' or 'goodbye' to exit.

## Code Example

Example snippet from chatbot_response function:

if any(greet in user_input for greet in ['hello', 'hi', 'hey']):
return "Hello! How can I help you today?"

text

## Extending the Chatbot

- Add new keywords and responses in the `chatbot_response` function.
- Improve math expression parsing for more complex calculations.
- Integrate external APIs (weather, news, etc.) for dynamic content.
- Use NLP libraries for more advanced language understanding.

## License

This project is open source and free to use for learning and personal projects.

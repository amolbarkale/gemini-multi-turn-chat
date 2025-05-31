import os
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env")
        return

    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Initialize Gemini model
    model = genai.GenerativeModel("gemini-2.0-flash-001")

    # Set system prompt (fixed)
    system_prompt = "You are a helpful assistant who answers questions clearly and politely."

    # Get user prompt from input
    user_input = input("Enter your question: ")

    # Combine system + user prompt
    full_prompt = f"{system_prompt}\nUser: {user_input}"

    # Generate response with token tracking
    response = model.generate_content(full_prompt)

    # Output response and token usage
    print("\nAssistant:", response.text)
    print("\n[Token Usage Not Available in Gemini API Yet]")

if __name__ == "__main__":
    main()
#########################################################################

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Optional: Ask user for temperature (or use default)
temp_input = input("Set model temperature (0.0 - 2.0, default 0.7): ")
try:
    temperature = float(temp_input.strip()) if temp_input.strip() else 0.7
except ValueError:
    temperature = 0.7

# Initialize chat model with context tracking
gemini = genai.GenerativeModel("gemini-2.0-flash-001")
chat = gemini.start_chat(history=[])

# Turn 1
user_input_1 = input("You: ")
response_1 = chat.send_message(user_input_1, generation_config={"temperature": temperature})
print("Gemini:", response_1.text)

# Turn 2
user_input_2 = input("You: ")
response_2 = chat.send_message(user_input_2, generation_config={"temperature": temperature})
print("Gemini:", response_2.text)

# Bonus: Turn 3 (optional)
turn_3 = input("Would you like to continue the conversation? (yes/no): ")
if turn_3.lower().startswith("y"):
    user_input_3 = input("You: ")
    response_3 = chat.send_message(user_input_3, generation_config={"temperature": temperature})
    print("Gemini:", response_3.text)

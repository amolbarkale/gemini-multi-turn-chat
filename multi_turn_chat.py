import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# Optional: Ask user for temperature (or use default)
temp_input = input("Set model temperature (0.0 - 2.0, default 0.7): ")
try:
    temperature = float(temp_input.strip()) if temp_input.strip() else 0.7
except ValueError:
    temperature = 0.7

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

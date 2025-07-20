import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose the model to use
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Function to interact with AYUSH (Gemini)
def talk_with_ayush(prompt):
    try:
        if not prompt:
            return "❌ Empty prompt received."

        response = model.generate_content(prompt)
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "❌ No response text received from Gemini."

    except Exception as e:
        return f"❌ Gemini Error: {str(e)}"

"""Test the new Google GenAI SDK."""

from dotenv import load_dotenv
import os

from google import genai

# Load .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key Loaded:", api_key is not None)

client = genai.Client(api_key=api_key)

print("✅ google-genai imported successfully.")
print("✅ Client created successfully.")
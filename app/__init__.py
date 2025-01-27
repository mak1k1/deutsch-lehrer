from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Optional: Access the API key to ensure it's loaded
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("DEEPSEEK_API_KEY is missing. Please check your .env file.")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
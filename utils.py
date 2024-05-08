import os
from dotenv import load_dotenv




def get_llm_keys():
    load_dotenv()
    open_ai_key = os.getenv("OPENAI_API_KEY")
    groq_ai_key = os.getenv("GROQ_API_KEY")
    return (open_ai_key, groq_ai_key)
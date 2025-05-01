from openai import OpenAI
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def translate_text(text, target_language):
    prompt = f"Translate the following text to {target_language}: {text}"
    completion = client.chat.completions.create(
        model='deepseek/deepseek-r1:free',
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
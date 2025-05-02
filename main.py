from openai import OpenAI
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# Initialize FastAPI client
app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    target_language: str="German"

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


@app.post("/translate")
async def translate(request: TranslationRequest):
    try:
        translated_text = translate_text(request.text, request.target_language)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
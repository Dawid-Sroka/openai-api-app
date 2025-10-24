from fastapi import FastAPI
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    completion = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "user",
                "content": "Say hi",
            },
        ]
    )
    return {"message": completion.choices[0].message.content}
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from fastapi.responses import JSONResponse
from .helper import get_user_stories
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/analyse")
async def analyse(prompt: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()  # You can process the file here if needed

    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "Generate user stories from the given input."},
    #         {"role": "user", "content": prompt},
    #     ],
    # )

    # return {"stories": response["choices"][0]["message"]["content"]}
    with open('output.json') as f:
        json_data = json.load(f)
    response = get_user_stories(json_data)
    return JSONResponse(content={"response":response})

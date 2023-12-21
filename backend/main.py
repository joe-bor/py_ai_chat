# uvicorn main:app
# uvicorn main:app --reload

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages

# Initiate App
app = FastAPI()


# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000"
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Endpoints
@app.get("/")
async def root():
    return {"message": "Hello This is the root path!"}


@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation has been reset"}


@app.get("/health")
async def check_health():
    return {"message": "check_health() invoked"}


# Send Audio File
# Note: Not playing in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):
#     print("hello")


@app.get("/post-audio-get/")
async def get_audio():
    
    # Open audio file -- with context manager ???
    audio_input = open("voice_test.mp3", "rb")
    
    # Decode audio with Whisper
    transcribed_text = convert_audio_to_text(audio_input)
    
    # Guard
    if not transcribed_text:
        return HTTPException(status_code=400, detail="Failed to decode audio")
    
    # Talk to ChatGPT
    chat_response = get_chat_response(transcribed_text)
    
    # Store messages in db
    store_messages(transcribed_text, chat_response)
    
    print(f"chat_response: {chat_response}")
    
    return transcribed_text
    
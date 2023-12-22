from openai import OpenAI
from decouple import config
from pprint import pprint

# Import custom functions
from functions.database import get_recent_messages

# Retrieve environment variables
organization = config("OPENAI_ORG_ID")
api_key = config("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key,
    organization=organization
)



# Convert Audio to text using OpenAI - Whisper
def convert_audio_to_text(audio_file):
    try:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file            
        )
        
        return transcript.text
    
    except Exception as e:
        print(e)
        return
    
# Open AI- Chat GPT
# Get response to our message

def get_chat_response(message_input):
    
    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)

    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        message_text = response.choices[0].message.content
        
        return message_text
    except Exception as e:
        print(e)
        return
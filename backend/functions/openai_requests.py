from openai import OpenAI
from decouple import config

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
        print(f"transcript: {transcript}")
        
        return transcript.text
    except Exception as e:
        print(e)
        return
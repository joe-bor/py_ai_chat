import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")


# Convert text to speech
def convert_text_to_speech(message):
    
    url = "https://api.elevenlabs.io/v1/text-to-speech/MF3mGyEYCl7XYWbV9V6O"
    
    body = {
        "text": message,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "similarity_boost": 0.5,
            "stability": 0.5
        }
        
    }
    
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }
    
    # Send request
    try:
        response = requests.request("POST", url, json=body, headers=headers)
    except Exception as e:
        print(e)
        return
    
    # Handle response
    if response.status_code == 200:
        return response.content
    else:
        return
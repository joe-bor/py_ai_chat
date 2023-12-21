import json
import random

# Get recent messages

def get_recent_messages():
    '''
    This function fetches the last 10 messages between the user and the chat bot.
    '''
    
    # Define the file name and learn instruction
    # TODO: Fetch this data from DB in production
    file_name = "stored_data.json"
    learn_instructions = {
        "role": "system",
        "content": "You are interviewing the user for a job as a junior software engineer. Ask them to introduce themselves to get an idea of their background and the skills and experience they've gained. Then with the information you obtain, create relevant questions that are normally asked in software engineering job interviews at a junior level. Keep your answers/questions short, max of 30 words."
    }
    
    # Initialize messages
    messages = []
    
    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instructions["content"] += "Your response will include dry humor."
    else:
        learn_instructions["content"] += "Your response will include a challenging question."
        
    # Append instruction to messages
    messages.append(learn_instructions)
    
    # Get last messages
    # TODO: This process will also be affected when in prod, depending on how we store messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            print(f"data: {data}") # !DELETE
            # Append last 10 items of data
            if data:
                if len(data) < 10:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-10:]:
                        messages.append(item)
    except Exception as e:
        print(e)

    return messages


def store_messages(request_message, response_message):
    
    # Define the file name
    # TODO: Change this when we move our convos in a db
    file_name = "stored_data.json"
    
    # Get recent messages
    messages = get_recent_messages()[1:]
    
    # Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)
    
    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)
    
    
# Reset messages
def reset_messages():
    # Overwrite with nothing == Reset
    with open('stored_data.json', 'w') as file:
        pass
    
# https://www.udemy.com/course/chatgpt-ai-voice-chatbot-build-with-react-and-fast-api-combo/learn/lecture/36923404#overview
# https://platform.openai.com/docs/guides/text-generation/chat-completions-api
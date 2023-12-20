import json
import random

# Get recent messages

def get_recent_message():
    '''
    This function fetches the last 10 messages between the user and the chat bot.
    '''
    
    # Define the file name and learn instruction
    # TODO: Fetch this data from DB in production
    file_name = "stored_data.json"
    learn_instructions = {
        "role": "system",
        "content": "You are interviewing the user for a job as a junior software engineer. Ask them to introduce themselves to get an idea of their background and the skills and experience they've gained. Then with the information you obtain, create relevant questions that are normally asked in software engineering job interviews at a junior level. Keep your answers/questions short."
    }
    
    # Initialize messages
    messages = []
    
    # Add a random element
    x = random.uniform()
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


from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#print models you can use
# models = client.models.list()

# for m in models:
#     print(m.name)

def generate_welcome_message(user):

    prompt = f"""
    Create a friendly welcome message.

    Username: {user['username']}
    Hobby: {user['hobby']}

    Keep it short and friendly and at least 50 words.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    #print('response', response)
    return response.text


def generate_birthday_wishes(user):
    """Generate personalized birthday wishes based on user information"""
    
    prompt = f"""
    Create a warm, personalized, and heartfelt birthday wish message.

    Username: {user['username']}
    Hobby: {user['hobby']}
    
    The message should:
    - Be warm and celebratory
    - Mention their hobby to make it personal
    - Include positive wishes for their future
    - Be between 2-3 sentences
    - Use celebratory emojis
    
    Just write the birthday message, at least 50 words.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text
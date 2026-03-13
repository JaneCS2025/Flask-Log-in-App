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

    Keep it short and friendly and no more than 20 words.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print('response', response)
    return response.text
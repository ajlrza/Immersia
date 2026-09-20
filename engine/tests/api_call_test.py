import os
from google import genai

# Initial test, uses gemini for conveniency
def test_api_gemini_call(message: str):
    key = os.environ.get("KEY")

    client = genai.Client(api_key=key)
    chat = client.chats.create(model='gemini-2.0-flash')
    response = chat.send_message('tell me')
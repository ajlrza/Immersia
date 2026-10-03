# THIRD PARTY - HUGGINGFACE
import json, requests, base64
from huggingface_hub import HfApi
from huggingface_hub import login, DeviceCodeError

# ENGINE MODULE
from engine_dataclasses.main_dc import (EnginePayload, PromptPayload)

# thinking of getting inspiration from IPv6 neighbor solicit and broadcasting

# Build a unified middleware service hosted on different soon so if errors occur it wont hit the app

headers = {"Authorization": os.getenv("API_CALLER_TOKEN")} 

async def api_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []
  
#  try:
#    login(api_key)
#    hf_api = HfApi()
#
#  except ValueError:
#    return ValueError
  
#  except DeviceCodeError:
#    return DeviceCodeError
  
async def openai_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
)  -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def anthropic_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
)  -> json:
  
  sdk_api: object
  hf_api: object
  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass
  
async def google_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object
  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def mistral_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object
  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def cohere_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def perxplexity_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def openrouter_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def groq_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def together_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def hf_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def deepinfra_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def azure_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def aws_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass

async def vertex_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  sdk_api: object
  hf_api: object

  try:

    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if data.status == 200:

        encoded_content = data["content"]
        decoded_code = base64.b64decode(encoded_content).decode("utf-8")
        
        return {
            "Action": "",
            "Avatar": "",
            "Position": "",
            "World": "",
            "Metadata": {}
        }

  except:
        pass

  encoded_content = data["content"]
  decoded_code = base64.b64decode(encoded_content).decode("utf-8")

  if (doRender):
    image: bytearray = []

  pass
# THIRD PARTY - HUGGINGFACE
import orjson, json, requests, base64, struct, os, typing, types
from huggingface_hub import HfApi
from huggingface_hub import login, DeviceCodeError

# ENGINE MODULE
from engine_dataclasses.main_dc import (EnginePayload, PromptPayload)
from engine.llm.state_construction import constructor

# thinking of getting inspiration from IPv6 neighbor solicit and broadcasting

# Build a unified middleware service hosted on different soon so if errors occur it wont hit the app


TOON_TEMPLATE = "->compressworldusing->worldtheme:[list],generalkwords:[list],charactersname:[list]ifany->worldconnect[theme,characters,keywords]"

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
)  -> orjson:
  
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
    model: str,
    endpoint: str,
    api_key: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    doRender: bool = False
) -> dict[str, typing.Any] | dict[str, bool]:

  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": api_key
  }

  payload = {
    "contents": [
        {
          "parts": [
              {
                "text": f"generatewrldsettng->'{content}'->text",
                "text": f"follow->{TOON_TEMPLATE}->imgrep&3bgimgasprmpt",
                "text": "dontoverdoany"}
          ]
        }
    ],
    "generationConfig": {
      "responseModalities": ["TEXT","IMAGE"]
    }
  }

  # Soon
  #binary_obj: struct.Struct = struct.pack(headers, payload)

  try:

    response = requests.get(
      url=endpoint, 
      headers=headers,
      data=orjson.dumps(payload)
      )

    data = orjson.loads(response.raw())

    if (isinstance(data, dict[str, any])):
      data = data["content"]
    elif (not isinstance(data, object)):
      return {"Error": "orjson parsing"}
        
    if (content == first_prompt):
      constructor.setting_state_assemble(encoded_content)
      data = d
    elif (content == user_states):
      constructor.overall_state_assemble(user_states, base64.b64decode(encoded_content).decode("utf-8"))

    return data

  except:
      return {"Error": "api request"}

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
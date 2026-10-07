# THIRD PARTY - HUGGINGFACE
import orjson, json, requests, base64, struct, os, typing, types
from huggingface_hub import HfApi
from huggingface_hub import login, DeviceCodeError

# ENGINE MODULE
from engine_dataclasses.main_dc import (EnginePayload, PromptPayload)
from engine.llm.state_construction import constructor

# thinking of getting inspiration from IPv6 neighbor solicit and broadcasting

# Build a unified middleware service hosted on different soon so if errors occur it wont hit the app


WORLD_BUILD_TOON_TEMPLATE = "->compressworldusing->worldtheme:[list],generalkwords:[list],charactersname:[list]ifany->worldconnect[theme,characters,keywords]"
WORLD_PROGRESS_TOON_TEMPLATE = "->compressworldusing->generalstate:str[state1,2,3]mcavatarstate:str[emotion1,2,3],mcpositionstate:float[x,y,z],worldstate->[events->variables]"  
STANDARD_HEADERS = {'Content-Type': 'application/json'}

async def response_handler(endpoint: str, headers: str):
    
    try:

      response = requests.get(
        url=endpoint, 
        headers=headers,
        timeout=5)

      if (response.elapsed.total_seconds() >= 1):
        print("Response timeout after 5 seconds.")

      if response.status_code == 200:

          data = orjson.loads(response.raw)

          if (isinstance(data, dict[str, any])):
            data = data["content"]
          elif (not isinstance(data, object)):
            return {"Error": "orjson parsing"}
          return data
          
    except:
      return {"Error": "response"}

async def openai_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
)  -> json:
  
  sdk_api: object
  hf_api: object

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

async def anthropic_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
)  -> orjson:
  
  sdk_api: object
  hf_api: object

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)
  
async def google_call(
    model: str,
    endpoint: str,
    api_key: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    doRender: bool = False
) -> dict[str, typing.Any] | dict[str, bool]:

  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  payload = {
    "contents": [
        {
          "parts": [
              {
                "text": f"generatewrldsettng->'{content}'->text",
                "text": f"follow->{WORLD_BUILD_TOON_TEMPLATE}->imgrep&3bgimgasprmpt",
                "text": "dontoverdoany"}
          ]
        }
    ],
    "generationConfig": {
      "responseModalities": ["TEXT","IMAGE"]
    }
  }

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  # Soon
  #binary_obj: struct.Struct = struct.pack(headers, payload)

  response = response_handler(endpoint, exclusive_headers)

  return response

async def mistral_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:

  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS
  
  response = response_handler(endpoint, exclusive_headers)

  return response

async def cohere_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response

async def perxplexity_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response

async def openrouter_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response

async def groq_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response

async def together_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response

async def hf_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response

async def deepinfra_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response

async def azure_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response

async def aws_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response
async def vertex_call(
    endpoint: str,
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
) -> json:
  
  content: EnginePayload | PromptPayload | None = user_states or first_prompt or None

  exclusive_headers = {}
  exclusive_headers |= STANDARD_HEADERS

  response = response_handler(endpoint, exclusive_headers)

  return response
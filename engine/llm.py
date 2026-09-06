import os, websockets
from huggingface_hub import HfApi
from huggingface_hub import login, DeviceCodeError
from .engine_dc import (
  EnginePayload,
  PromptPayload,
  Data
)

# Build a unified middleware service hosted on different soon so if errors occur it wont hit the app
API_KEY_CATALOG: set[str] = {
  'OPENAI', 
  'ANTHROPIC', 
  'GOOGLE', 
  'MISTRAL', 
  'COHERE', 
  'PERPLEXITY',
  'OPENROUTER',
  'GROQ',
  'TOGETHER',
  'HF'
  'DEEPINFRA',
  'AZURE-OAI',
  'AWS',
  'VERTEX',
  }

async def api_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
    ):
  
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
  
  

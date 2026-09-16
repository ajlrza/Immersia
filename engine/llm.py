import os, websockets
from huggingface_hub import HfApi
from huggingface_hub import login, DeviceCodeError
from engine_dataclasses.main_dc import (
  EnginePayload,
  PromptPayload,
  Data
)

# thinking of getting inspiration from IPv6 neighbor solicit and broadcasting

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
  
async def openai_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def anthropic_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass
  
async def google_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def mistral_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def cohere_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def perxplexity_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def openrouter_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def groq_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def together_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def hf_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def deepinfra_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def azure_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def aws_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass

async def vertex_call(
    user_states: EnginePayload = None, 
    first_prompt: PromptPayload = None, 
    api_key: str = None, 
    doRender: bool = False
):
  
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []

  pass
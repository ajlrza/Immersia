# THIRD PARTY - HUGGINGFACE
from huggingface_hub import HfApi
from huggingface_hub import login, DeviceCodeError

# ENGINE MODULE
from engine_dataclasses.main_dc import (EnginePayload, PromptPayload)

# thinking of getting inspiration from IPv6 neighbor solicit and broadcasting

# Build a unified middleware service hosted on different soon so if errors occur it wont hit the app

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
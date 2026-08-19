import process
from huggingface_hub import HfApi
from huggingface_hub import login
import GoogleGenAI from '@google/genai';

async def api_call(states: object, api_key: str, doRender: bool = False):
  sdk_api: object
  hf_api: object

  if (doRender):
    image: bytearray = []
  
  try:
    sdk_api = GoogleGenAI(api_key)
  except:
    login(api_key)
    hf_api = HfApi()
  
  llm = GoogleGenAI();
  response = await llm.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: {
        user: 'states',
        system: 'states_prompt'
    }  
   })

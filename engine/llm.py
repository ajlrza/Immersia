import process
from huggingface_hub import HfApi
from huggingface_hub import login
import GoogleGenAI from '@google/genai';

def api_call(doRender: boolean = False, states: object, api_key: string):
  sdk_api: object
  hf_api: object
  
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

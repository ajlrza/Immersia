import process
import GoogleGenAI from '@google/genai';

def api_call(doRender: boolean = False, states: object):
  llm = GoogleGenAI();
  response = await llm.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: {
        user: 'states',
        system: 'states_prompt'
    }  
   })

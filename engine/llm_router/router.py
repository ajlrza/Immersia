import requests, websockets
from dataclasses import dataclasses
from engine_dataclasses.main_dc import (EnginePayload, PromptPayload)

UNIVERSAL_REQUEST = "POST /v1/chat/completions"

def WMRoute():
    pass

def Broadcast(key: str = None, model: str = None):
    
    if key == None and model == None:
        WMRoute()
        return # Fallback to custom world model

    if key and model:
        pass
    elif key and not model:
        pass
    elif not key and model:
        pass
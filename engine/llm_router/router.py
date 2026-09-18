import requests, websockets, base64, os, json
from typing import Any
from dataclasses import dataclasses
from engine_dataclasses.main_dc import (EnginePayload, PromptPayload)
from llm_router.storage import store

UNIVERSAL_REQUEST = "POST /v1/chat/completions"
STORE_PATH = "/storage/store.json"

class CatalogChecker:

    def __init__(self):
        self.Catalog = store.MODEL_CATALOG

    def __contains__(self, Key: str):

        if Key in self.Catalog:

            upperCaseKey = Key.upper()
            providerMetadata = getattr(store, upperCaseKey, None) 

            return providerMetadata

catalogChecker = CatalogChecker()

def WMRoute():
    pass

PROVIDER_CONFIG: any = None

def LoadStore() -> Any:

    if os.path.exists(STORE_PATH):
        try:

            with open(STORE_PATH, 'r') as f:

                PROVIDER_CONFIG = json.load(f)
                return PROVIDER_CONFIG

        except json.JSONDecodeError:
            assert json.JSONDecodeError

    return None

def UpdateStore(Config: str, Value: str, Model: str = None) -> bool | None:

    ConfigKeys: set[str] = ['ContextWindow', 'OperationStatus', 'RPM', 'PREFIX']

    if Config in ConfigKeys and Model:

        setattr(store, Model, Value)
        updatedConfig = getattr(store, Model, None)
        
        if updatedConfig.__getattribute__(Config) == Config:
            return True
    else:
        assert "Config Key does not exist"

def CatalogCheck(paramToCheck: str, optParamToCheck: str = None) -> Any | None | list[Any | None]:
    
    checkedCatalog: Any | None

    if (optParamToCheck):

        checkedCatalog = catalogChecker.__contains__(paramToCheck)
        optCheckedCatalog = catalogChecker.__contains__(optParamToCheck)

        return [checkedCatalog, optCheckedCatalog]

    checkedCatalog = catalogChecker.__contains__(paramToCheck)

    if (checkedCatalog):
        return checkedCatalog
    else:
        return None

url = "https://github.com"
headers = {"Authorization": os.getenv("API_CALLER_TOKEN")} 

def CheckAPI(key: str = None, model: str = None):

    data: Any = None

    if key:
        response = requests.get(url, headers=headers)
        data = response.json()

    encoded_content = data["content"]
    decoded_code = base64.b64decode(encoded_content).decode("utf-8")

    pass

def Broadcast(key: str = None, model: str = None):
    
    if key == None and model == None:
        WMRoute()
        return # Fallback to custom world model

    if key and model:

        checkBoth = CatalogCheck(model, key)
        
        if checkBoth:

            checkForAPI = CheckAPI(checkBoth[0], checkBoth[1])

    elif key and not model:
        
        checkKey = CatalogCheck(key)

        if checkKey:

            checkForAPI = CheckAPI(checkKey)

    elif not key and model:
        
        return False
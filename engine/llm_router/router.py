import requests, websockets, base64, os, json
from typing import Any
import orjson
from dataclasses import dataclasses
from engine_dataclasses import main_dc
from llm_router.storage import store

UNIVERSAL_REQUEST = "POST /v1/chat/completions"
STORE_PATH = "/storage/store.json"
ROUTER_STATUSES: set[str] = {"NOT ROUTING", "ROUTING", "ROUTED"}
ROUTER_LAYERS: set[str] = {"NONE", "ENTRY", "CHECK", "LOAD", "UPDATE", "API", "RESPONSE"}
CONFIG_KEYS: set[str] = ['ContextWindow', 'OperationStatus', 'RPM', 'PREFIX']

# If Router Status is Routed, we're done and clear result data
RouterStatus: main_dc.RouterStatus = {
    "Status": "NOT ROUTING",
    "RouterLayer": "NONE"
}


class CatalogChecker:

    def __init__(self):
        self.Catalog = store.MODEL_CATALOG

    def __contains__(self, Key: str):

        if Key in self.Catalog:

            upperCaseKey = Key.upper()
            # Checks the actual python code file
            providerMetadata = getattr(store, upperCaseKey, None) 

            return providerMetadata

catalogChecker = CatalogChecker()

def WMRoute():
    pass

PROVIDER_CONFIG: any = None

def UpdateJSONStore(Config: str, Value: str, Model: str = None) -> bool:

    if os.path.exists(STORE_PATH):
        try:

            with open(STORE_PATH, 'r') as f:

                PROVIDER_CONFIG = orjson.loads(f)

                return True

        except orjson.JSONDecodeError:
            raise orjson.JSONDecodeError

    return None

def UpdatePyStore(Config: str, Value: str, Model: str = None) -> bool | orjson.JSONDecodeError | AssertionError:

    if (RouterStatus.Status):
        return False # Or we can wait here or default fallback?

    if Config in CONFIG_KEYS and Model:

        RouterStatus.Status = "NOT ROUTING"
        RouterStatus.RouterLayer = "UPDATE"

        setattr(store, Model, Value)
        updatedConfig = getattr(store, Model, None)
        
        if updatedConfig.__getattribute__(Config) == Config:

            DoJSONNext = UpdateJSONStore(Config, Value, Model)

            if (DoJSONNext):
                RouterStatus.Status = "NONE"
                return True
  
        else:
            RouterStatus.Status = "NONE"
            raise AssertionError("Config was not updated in .py file")
    else:
        RouterStatus.Status = "NONE"
        raise AssertionError("Config Key does not exist")

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

def CheckAPI(key: str = None, model: str = None) -> bool:

    data: Any = None

    if key:
        response = requests.get(url, headers=headers)
        data = response.json()

    encoded_content = data["content"]
    decoded_code = base64.b64decode(encoded_content).decode("utf-8")

    pass

def Broadcast(key: str = None, model: str = None) -> bool:

    if not key and model:
        return False

    if (RouterStatus.Status == "ROUTING"):
        return False
    elif (RouterStatus.Status == "NOT ROUTING" and RouterStatus.RouterLayer not in {"UPDATE", "LOAD", "API"}):
        RouterStatus.Status = "ROUTING"
    
    if key == None and model == None:
        RouterStatus.Status = "ROUTING"
        WMRoute()
        return # Fallback to custom world model

    if key and model:

        RouterStatus.RouterLayer = "CHECK"
        checkBoth = CatalogCheck(model, key)
        
        if checkBoth:

            RouterStatus.RouterLayer = "API"
            checkForAPI = CheckAPI(checkBoth[0], checkBoth[1])

    elif key and not model:
        
        RouterStatus.RouterLayer = "CHECK"
        checkKey = CatalogCheck(key)

        if checkKey:

            RouterStatus.RouterLayer = "API"
            checkForAPI = CheckAPI(checkKey)

def RouterEntrypoint(Payload: main_dc.EnginePayload | main_dc.PromptPayload) -> bool:

    # Check for router status first

    if (RouterStatus.Status == "ROUTING"):
        return False # avoid race condition

    elif (RouterStatus.Status == "ROUTED"):
        RouterStatus.Status = "NOT ROUTING"

    SentBroadcast: bool | dict[str, main_dc.APIConfig] = Broadcast(Payload.Key | Payload.Model)

    if (not SentBroadcast):
        return False

    elif (SentBroadcast):
        RouterStatus.Status = "ROUTED"
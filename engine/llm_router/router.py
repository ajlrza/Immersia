import requests, websockets, base64, os, json
import typing, types
from typing import Literal
import orjson
from dataclasses import dataclasses
from engine_dataclasses import main_dc
from llm_router.storage import store

UNIVERSAL_ENDPOINT = "/v1/chat/completions"
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

    def __contains__(self, Model: str):

        if Model in self.Catalog:

            upperCaseModel = Model.upper()
            # Checks the actual python code file
            providerMetadata = getattr(store, upperCaseModel, None) 

            return providerMetadata

catalogChecker = CatalogChecker()

PROVIDER_CONFIG: any = None

def UpdateJSONStore(Config: str, Value: str, Model: str = None) -> bool:

    if os.path.exists(STORE_PATH):
        try:

            with open(STORE_PATH, 'w') as JSONStore:

                PROVIDER_CONFIG = orjson.loads(JSONStore)
                

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

def CatalogCheck(paramToCheck: str, optParamToCheck: str = None) -> typing.Any | None | list[typing.Any | None]:
    
    checkedCatalog: typing.Any | None

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

def CheckAPI(key: str = None, model: str = None) -> Literal['UP', 'DOWN']:

    Model: str | None
    Key: str | None

    if model:
        Model = model.upper()

    # Checks the actual python code file
    providerMetadataStatus = getattr(store, Model.__getattribute__('Status'), None) 

    if providerMetadataStatus.__getattribute__('LastUpdate')  > 365:
        print("Potentially depracated AI API and Model, use at own risk.")

    if (providerMetadataStatus == 'DOWN'):
        return 'DOWN'
    
    return 'UP'

def CallAPI(endpoint: str) -> main_dc.EnginePayload:

    try:

        RouterStatus.RouterLayer = 'API'

        response = requests.get(endpoint, headers=headers)
        data = response.json()

        if data.status == 200:

            encoded_content = data["content"]
            decoded_code = base64.b64decode(encoded_content).decode("utf-8")
            
            return {
                "Action": "",
                "Avatar": "",
                "Position": "",
                "World": "",
                "Metadata": {}
            }

    except:
        pass

    encoded_content = data["content"]
    decoded_code = base64.b64decode(encoded_content).decode("utf-8")

def Broadcast(Payload: main_dc.EnginePayload | main_dc.PromptPayload):

    if len(Payload.Prompt() > 10000):
        # Broadcast who can handle ts
        pass

def Route(key: str = None, model: str = None) -> main_dc.EnginePayload | types.Callable:

    if isinstance(key, types.NoneType) and isinstance(key, types.NoneType):
        
        # Let's see which model can handle instead
        RouterStatus.Status = "BROADCASTING"
        return Broadcast

    if (RouterStatus.Status == "ROUTING"):
        return False
    elif (RouterStatus.Status == "NOT ROUTING" and RouterStatus.RouterLayer not in {"UPDATE", "LOAD", "API"}):
        RouterStatus.Status = "ROUTING"
    
    if isinstance(key, str) and isinstance(model, str):

        RouterStatus.RouterLayer = "CHECK"
        checkBoth = CatalogCheck(model, key)

        try:
            RouterStatus.RouterLayer = "API"
            
            assert isinstance(checkBoth, list) == True, "Model configuration does not exist"
            assert all(isinstance(catalog, object) for catalog in checkBoth) == True, "Listed catalog is not an object"

            if len(checkBoth == 1):
                checkedForAPI = CheckAPI(checkBoth[0])

                if (checkedForAPI == 'UP'):
                    return CallAPI(endpoint="https://" + model.lower() + UNIVERSAL_ENDPOINT)
                elif (checkedForAPI == 'DOWN'):
                    return Broadcast

            checkedForAPI = CheckAPI(checkBoth[0], checkBoth[1])

            if (checkedForAPI == 'UP'):
                return CallAPI(endpoint="https://" + model.lower() + UNIVERSAL_ENDPOINT)
            elif (checkedForAPI == 'DOWN'):
                return Broadcast

        except AssertionError as e:
            print(str(e) + ", searching on huggingface... ")


    elif key and not model:
        
        RouterStatus.RouterLayer = "CHECK"
        checkKey = CatalogCheck(key)

        if checkKey:

            RouterStatus.RouterLayer = "API"
            checkedForAPI = CheckAPI(checkKey)

            if (checkedForAPI == 'UP'):
                return CallAPI(endpoint="https://" + model.lower() + UNIVERSAL_ENDPOINT)
            elif (checkedForAPI == 'DOWN'):
                return Broadcast
            
def Router(Payload: main_dc.EnginePayload | main_dc.PromptPayload) -> main_dc.EnginePayload:

    # Check for router status first

    if (RouterStatus.Status == "ROUTING"):
        return False # avoid race condition

    elif (RouterStatus.Status == "ROUTED"):
        RouterStatus.Status = "NOT ROUTING"
    
    RoutedRequest: main_dc.EnginePayload | types.Callable = None

    if (Payload.Prompt):
        RoutedRequest: main_dc.EnginePayload | types.Callable = Route(Payload.Key or Payload.Model)

        if isinstance(RoutedRequest, types.Callable):
            BroadcastedRequest = RoutedRequest(Payload)

        if RoutedRequest == 'DOWN':
            return False
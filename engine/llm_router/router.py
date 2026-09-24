# ENGINE MODULES
from llm_router.storage import store
from engine_dataclasses import main_dc

# NATIVE MODULES - TYPES 
import typing, types

# NATIVE MODULES - ROUTING 
import orjson, threading, asyncio

# NATIVE MODULES - NETWORK
import requests, websockets, base64, os

UNIVERSAL_ENDPOINT = "/v1/chat/completions"
STORE_PATH = "/storage/store.json"
ROUTER_STATUSES: set[str] = {"NOT ROUTING", "ROUTING", "ROUTED"}
ROUTER_LAYERS: set[str] = {"NONE", "ENTRY", "CHECK", "BROADCAST", "LOAD", "UPDATE", "API", "RESPONSE"}
CONFIG_KEYS: set[str] = ['ContextWindow', 'OperationStatus', 'RPM', 'PREFIX']

# If Router Status is Routed, we're done and clear result data

lock = asyncio.Lock()
RouterStatus: main_dc.RouterStatus 

async def UpdateRouterStatus(status: str = None, layer: str = None) -> bool:

    if (not status and not layer):
        print("No status and layer were passed.")
        return False

    await lock.acquire()

    global RouterStatus

    try:

        if (status and layer):

            RouterStatus.Status = status
            RouterStatus.Layer = layer

        elif (not layer and status):
            
            RouterStatus.Status = status

        elif (not status and layer):

            RouterStatus.Layer = layer

    except Exception as e:
        print(e)
        lock.release()
        assert e

    lock.release()
    return True

async def ReadRouterStatus(status: str = None, layer: str = None) -> bool:

    if (not status and not layer):
        print("No status and layer were passed.")
        return False

    await lock.acquire()

    global RouterStatus

    try:

        if (status and layer):

            assert status == RouterStatus.Status
            assert layer == RouterStatus.Layer

        elif (not layer and status):
            
            assert status == RouterStatus.Status
            
        elif (not status and layer):

            assert layer == RouterStatus.Layer

    except Exception as e:
        print(e)
        lock.release()
        return False

    lock.release()
    return True


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

async def UpdateJSONStore(Config: str, Value: str, Model: str = None) -> bool:

    if os.path.exists(STORE_PATH):
        try:

            with open(STORE_PATH, 'w') as JSONStore:

                PROVIDER_CONFIG = orjson.loads(JSONStore)
                
                return True

        except orjson.JSONDecodeError:
            raise orjson.JSONDecodeError

    return None

async def UpdatePyStore(Config: str, Value: str, Model: str = None) -> bool | orjson.JSONDecodeError | AssertionError:

    if Config in CONFIG_KEYS and Model:

        await UpdateRouterStatus(status='NOT ROUTING', layer='UPDATE')

        setattr(store, Model, Value)
        updatedConfig = getattr(store, Model, None)
        
        if updatedConfig.__getattribute__(Config) == Config:

            DoJSONNext = UpdateJSONStore(Config, Value, Model)

            if (DoJSONNext):
                UpdateRouterStatus(layer='NONE')
                lock.release()
                return True
  
        else:
            await UpdateRouterStatus(layer='NONE')
            raise AssertionError("Config was not updated in .py file")
    else:
        await UpdateRouterStatus(layer='NONE')
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

async def CheckAPI(model: str = None) -> typing.Literal['UP', 'DOWN']:

    Model: str | None

    if model:
        Model = model.upper()

    # Checks the actual python code file
    providerMetadataStatus = getattr(store, Model.__getattribute__('Status'), None) 

    if providerMetadataStatus.__getattribute__('LastUpdate')  > 365:
        print("Potentially depracated AI API and Model, use at own risk.")

    if (providerMetadataStatus == 'DOWN'):
        return 'DOWN'
    
    return 'UP'

async def CallAPI(endpoint: str) -> main_dc.EnginePayload:

    try:

        await UpdateRouterStatus(layer='API')

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

async def Route(key: str = None, model: str = None) -> main_dc.EnginePayload | types.Callable:

    if isinstance(key, types.NoneType) and isinstance(key, types.NoneType):
        
        # Let's see which model can handle instead
        await UpdateRouterStatus(layer='BROADCAST')
        return Broadcast

    if (RouterStatus.Status == "ROUTING"):
        return False
    elif (RouterStatus.Status == "NOT ROUTING" and RouterStatus.Layer not in {"UPDATE", "LOAD", "API"}):
        RouterStatus.Status = "ROUTING"
    
    if isinstance(key, str) and isinstance(model, str):

        await UpdateRouterStatus(layer='CHECK')
        checkBoth = CatalogCheck(model)

        try:
            await UpdateRouterStatus(layer='API')
            
            assert isinstance(checkBoth, list) == True, "Model configuration does not exist"
            assert all(isinstance(catalog, object) for catalog in checkBoth) == True, "Listed catalog is not an object"

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
        
        await UpdateRouterStatus(layer='CHECK')
        checkKey = CatalogCheck(key)

        if checkKey:

            await UpdateRouterStatus(layer='API')
            checkedForAPI = CheckAPI(checkKey)

            if (checkedForAPI == 'UP'):
                return CallAPI(endpoint="https://" + model.lower() + UNIVERSAL_ENDPOINT)
            elif (checkedForAPI == 'DOWN'):
                return Broadcast
            
def Router(Payload: main_dc.EnginePayload | main_dc.PromptPayload) -> main_dc.EnginePayload:

    # Check for router status first

    if ReadRouterStatus(layer='ROUTING'):
        return False 
        # avoid race condition

    elif ReadRouterStatus(layer='ROUTED'):
        RouterStatus.Status = "NOT ROUTING"
    
    RoutedRequest: main_dc.EnginePayload | types.Callable = None

    if (Payload.Prompt):
        RoutedRequest: main_dc.EnginePayload | types.Callable = Route(Payload.Key or Payload.Model)

        if isinstance(RoutedRequest, types.Callable):
            BroadcastedRequest = RoutedRequest(Payload)

        if RoutedRequest == 'DOWN':
            return False
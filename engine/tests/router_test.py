import unittest
from engine_dataclasses.main_dc import EnginePayload
from llm_router.router import (
    Router, 
    Route, 
    Broadcast, 
    CallAPI, 
    CheckAPI, 
    CatalogCheck, 
    UpdatePyStore, 
    UpdateJSONStore,
    UpdateRouterStatus,
    ReadRouterStatus
)

MOCK_ROUTER_STATUS = {
    "Status": "ROUTED",
    "Layer": "BROADCAST"
}

MOCK_PAYLOAD: EnginePayload = {
    "Action": "I moved over to the table",
    "Avatar": "Smiled happily",
    "Position": "",
    "World": "",
    "Metadata": "",
}

MOCK_EXTENDED_PAYLOAD = {
    "Action": "",
    "Avatar": "",
    "Position" "":,
    "World": "",
    "Ext": "",
    "Metadata": "",
}

def test_router():
    
    Router()
    pass

def test_route():

    Route()
    pass

def test_broadcast():

    Broadcast()
    pass

def test_call():

    CallAPI()
    pass

def test_check():

    CheckAPI()
    pass

def test_catalog():
    
    CatalogCheck()
    pass

def test_pystore():

    UpdatePyStore()
    pass

def test_jsonstore():

    UpdateJSONStore()
    pass

async def test_write_status():

    await UpdateRouterStatus()
    pass

async def test_read_status():

    await ReadRouterStatus()
    pass
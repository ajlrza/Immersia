import os
from typing import Literal
from dataclasses import dataclass, fields


@dataclass
class EnginePayload(slots=True):
    Action: str
    Avatar: str
    State: str
    World: str

@dataclass
class PromptPayload(slots=True):
    Prompt: str
    Metadata: str
    Key: str
    Model: str

@dataclass
class PerfPayload(slots=True):
    PercUsed: float
    Data: str  

@dataclass
class Data(slots=True):
    pass

@dataclass
class ContextWindow(slots=True):
    Tier: Literal["Free", "Commercial", "Enterprise", "Pro", "Community"] 
    Amount: int

@dataclass
class OperationStatus(slots=True):
    Status: str
    LastUpdate: int

@dataclass
class APIConfig(slots=True):
    Window: ContextWindow
    Status: OperationStatus
    RPM: int
    PREFIX: str

@dataclass
class RouterStatus(slots=True):
    Status: Literal["NOT ROUTING", "ROUTING", "ROUTED"]
    RouterLayer: Literal["ENTRY", "CHECK", "LOAD", "UPDATE", "API", "RESPONSE"]

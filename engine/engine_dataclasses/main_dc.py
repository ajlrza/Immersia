import os
from typing import Literal
from dataclasses import dataclass, fields

@dataclass
class InteractionMetadata(slots=True):
    EventWhen:      str
    GraphMasterID:  int # Master identifier responsible for placing the interaction data
    GraphNodes:     int # How many graph nodes, used for optimizing and storing properly
    StatesAffected: int # How many states affected, used also for optimizing and compress
    EngineStatus:   str # Engine status as of this interaction

@dataclass
class EnginePayload(slots=True):
    Action:     object
    Avatar:     object
    Position:   object
    World:      object
    Metadata:   InteractionMetadata

@dataclass
class PromptPayload(slots=True):
    Prompt:   str
    Metadata: str
    Key:      str
    Model:    str

@dataclass
class PerfPayload(slots=True):
    PercUsed: float
    Data:     str  

@dataclass
class Data(slots=True):
    pass

@dataclass
class ContextWindow(slots=True):
    Tier:   Literal["Free", "Commercial", "Enterprise", "Pro", "Community"] 
    Amount: int

@dataclass
class OperationStatus(slots=True):
    Status:     str
    LastUpdate: int

@dataclass
class APIConfig(slots=True):
    Window: ContextWindow
    Status: OperationStatus
    RPM:    int
    PREFIX: str

@dataclass
class RouterStatus(slots=True):
    Status:         Literal["NOT ROUTING", "ROUTING", "ROUTED"]
    Layer:          Literal["ENTRY", "CHECK", "LOAD", "UPDATE", "API", "RESPONSE"]

@dataclass
class EngineResponse:
    Context:    str
    Payload:    EnginePayload
    ByteData:   bytearray

@dataclass
class PacketHeader(slots=True):
    Version: int   
    Type:    int   
    Length:  int  
    ID:      int 

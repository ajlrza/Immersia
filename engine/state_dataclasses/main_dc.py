import os
import typing, types
from dataclasses import dataclass, field
from engine.engine_dataclasses import lmdb_dc
@dataclass
class PromptPayload(slots=True):
    Metadata:   object
    Prompt:     str
    Key:       str | None
    Model:     str | None


@dataclass
class GeneralState(slots=True):
    StateLinker:    dict[str, str | object]
    StateOne:       str
    StateTwo:       str
    StateThree:     str

@dataclass
class AvatarState(slots=True):
    StateLinker:    dict[str, str | object]
    EmotionOne:     str
    EmotionTwo:     str
    EmotionThree:   str

@dataclass
class PositionState(slots=True):
    StateLinker: dict[str, int | object]
    x:           int
    y:           int
    z:           int

@dataclass
class WorldState(slots=True):
    StateLinker:    dict[str, int | object]
    Event:          str
    Variables:      dict[str, str]

@dataclass
class EnginePayload(slots=True):
    General:    GeneralState
    Avatar:     AvatarState
    Position:   PositionState
    World:      WorldState
    Metadata:   lmdb_dc.InteractionMetadata

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
    Tier:   typing.Literal["Free", "Commercial", "Enterprise", "Pro", "Community"] 
    Amount: int

@dataclass
class OperationStatus(slots=True):
    Status:     str
    LastUpdate: int

@dataclass
class APIConfig(slots=True):
    Call: typing.Callable
    Window:     ContextWindow
    Status:     OperationStatus
    RPM:        int
    Prefix:     str
    Endpoint:   str

@dataclass
class RouterStatus(slots=True):
    Status:         typing.Literal["NOT ROUTING", "ROUTING", "ROUTED"]
    Layer:          typing.Literal["ENTRY", "CHECK", "LOAD", "UPDATE", "API", "RESPONSE"]

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

@dataclass
class ResourcePool(slots=True):
    
import os
import typing, types
from dataclasses import dataclass, field

@dataclass
class InteractionMetadata(slots=True):
    EventWhen:      str
    GraphMasterID:  int # Master identifier responsible for placing the interaction data
    GraphNodes:     int # How many graph nodes, used for optimizing and storing properly
    StatesAffected: int # How many states affected, used also for optimizing and compress
    EngineStatus:   str # Engine status as of this interaction

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
    Gravity:        int
    Force:          int
    Torque:         int
    Mass:           int
    Acceleration:   int

@dataclass
class EnginePayload(slots=True):
    General:    GeneralState
    Avatar:     AvatarState
    Position:   PositionState
    World:      WorldState
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
    
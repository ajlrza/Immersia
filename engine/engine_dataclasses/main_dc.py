import os
from dataclasses import dataclass, fields


@dataclass
class EnginePayload:
    Action: str
    Avatar: str
    State: str
    World: str

@dataclass
class PromptPayload:
    Prompt: str
    Metadata: str
    Key: str
    Model: str

@dataclass
class PerfPayload:
    PercUsed: float
    Data: str  

@dataclass
class Data:
    pass

@dataclass
class ContextWindow:
    Tier: str # Free, Commercial, Enterprise
    Amount: int

@dataclass
class OperationStatus:
    Status: str
    LastUpdate: str

@dataclass
class APIConfig:
    Window: ContextWindow 
    Status: OperationStatus
    RPM: int
    PREFIX: str

@dataclass
class RouterStatus:
    Status: str # NOT ROUTING | ROUTING | ROUTED
    RouterLayer: str # ENTRY | CHECK | LOAD | UPDATE | API | RESPONSE

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
    resources: float
    data: str  

@dataclass
class Data:
    pass

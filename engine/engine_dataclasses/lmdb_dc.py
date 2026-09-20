from dataclasses import dataclass, Fields, asdict
from datetime import datetime

@dataclass
class InteractionMetadata:
    EventWhen: datetime.date
    GraphMasterID: int # Master identifier responsible for placing the interaction data
    GraphNodes: int # How many graph nodes, used for optimizing and storing properly
    StatesAffected: int # How many states affected, used also for optimizing and compress
    EngineStatus: str # Engine status as of this interaction

@dataclass
class Interaction:
    Action: object
    Avatar: object
    Position: object
    World: object
    Ext: object | None
    Metadata: InteractionMetadata

from _typeshed import Incomplete
from typing import NamedTuple
from dataclasses import dataclass

class WorldPartition(NamedTuple):
    world: str
    partition: int

@dataclass
class StatePartition(slots=True):
    partition: list[dataclass] | dataclass

class VisorMetadata(NamedTuple):
    states_handled: int
    status: int

class PartitionMetadata(NamedTuple):
    topic: str
    offset: int
    leader_epoch: int | None
    replicas: list[int]

class StateMemberInformation(NamedTuple):
    member_id: str
    member_group: str

class StateGroupInformation(NamedTuple):
    group: str
    state: str
    members: list[StateMemberInformation]
    member_count: int

class RetryOptions(NamedTuple):
    limit: int
    backoff_ms: int
    retry_on_timeouts: bool


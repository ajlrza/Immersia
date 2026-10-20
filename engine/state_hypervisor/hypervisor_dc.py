from _typeshed import Incomplete
from typing import NamedTuple

class WorldPartition(NamedTuple):
    world: str
    partition: int

class StatePartition(NamedTuple):
    state: str
    partition: str

class VisorMetadata(NamedTuple):
    states_handled: int
    status: int

class PartitionMetadata(NamedTuple):
    topic: str
    partition: int
    leader: int
    leader_epoch: int | None
    replicas: list[int]
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

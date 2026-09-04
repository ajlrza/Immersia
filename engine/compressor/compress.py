import os
from dataclasses import dataclass, fields

@dataclass
class enginePayload:
    Action: str
    Avatar: str
    State: str
    World: str

@dataclass
class promptPayload:
    Prompt: str
    Metadata: str
    Key: str
    Model: str

def get_data(payload: object):
    pass


def get_bits(n):
    pass
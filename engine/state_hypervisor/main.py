from engine.engine_dataclasses import main_dc
from engine.state_hypervisor.hypervisor import CreateStatePartition, SendMainStates, SendBackgroundStates, SendMiscStates

# NATIVE MODULES - OS-LEVEL
import threading, os, multiprocessing

# THIRD PARTY - KAFKA
from kafka import KafkaConsumer, KafkaProducer
from kafka.structs import TopicPartition

OBSERVED = CreateStatePartition('OBSERVED', 0)
UNOBSERVED = CreateStatePartition('UNOBSERVED', 0)
MISC = CreateStatePartition('MISC', 0)

CPU_COUNT: int 
CPU_LEVEL: str | None 

CPU_ACTIVE: bool 
GPU_ACTIVE: bool 
MODEL_CACHE: str

PID: int 
current: object # Multiprocessing base process
children: list[object] # List of current base processes

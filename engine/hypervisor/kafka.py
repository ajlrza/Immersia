from engine.engine_dataclasses import main_dc

# NATIVE MODULES - OS-LEVEL
import threading, os, multiprocessing

# THIRD PARTY - KAFKA
from kafka import KafkaConsumer, KafkaProducer
from kafka.structs import TopicPartition

HARDWARE_PRIORITY = {
    "0.85": 0.85,
    "0.70": 0.70,
    "0.50": 0.50
}

OBSERVED = TopicPartition('OBSERVED', 0)
UNOBSERVED = TopicPartition('UNOBSERVED', 0)
MISC = TopicPartition('MISC', 0)

MODEL_CACHE: str

producer = KafkaProducer(bootstrap_servers='localhost:9092')

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')

consumer.assign([OBSERVED, UNOBSERVED, MISC])
consumer.poll

PID: int = os.getpid
current = multiprocessing.current_process
children = multiprocessing.active_children

CPU_LEVELS: set[str] = ["ONE_CORE", "MULTIPLE_CORES"]
CPU_COUNT: int = os.cpu_count() or 1
CPU_LEVEL: str | None = None 

if (CPU_COUNT == 1):
    print("Using default system level...")
    CPU_LEVEL = "ONE_CORE"

elif (CPU_COUNT > 1):
    print(f"Multiple cores detected, setting CPU_LEVEL to {"MULTPLE_CORES"}")
    CPU_LEVEL = "MULTIPLE_CORES"

ResourcePool: object

# OS-level, RAW IMPLEMENTATION IN PYTHON

## Entity-Data Actor: ResourcePoolManager
def ResourcePoolManager(payload: list[main_dc.EnginePayload, main_dc.PerfPayload]):
    pass

## Functions to initiate resources pool
def BeginPooling():
    pass

## Functions to take control of the resources pool

## Functions to standardize resources pool 

## Functions to create, delete,store, and change resources pool

## Functions to send to Kafka Topics depending on the resource pool manager

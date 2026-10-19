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

PID: int 
current: object # Multiprocessing base process
children: list[object] # List of current base processes

CPU_LEVELS: set[str] = ["ONE_CORE", "MULTIPLE_CORES"]

CPU_COUNT: int 
CPU_LEVEL: str | None 

CPU_ACTIVE: bool 
GPU_ACTIVE: bool 

ResourcePool: object

def CpuStatsConfigurator() -> bool:

    global CPU_ACTIVE
    global GPU_ACTIVE
    global PID
    global current
    global children
    global CPU_COUNT
    global CPU_LEVEL
    
    CPU_ACTIVE = True
    GPU_ACTIVE= False
    PID: int = os.getpid
    current = multiprocessing.current_process()
    children = multiprocessing.active_children()
    CPU_COUNT = os.cpu_count() or 1

    if (CPU_COUNT == 1):
        print("Using default system level...")
        CPU_LEVEL = "ONE_CORE"

    elif (CPU_COUNT > 1):
        print(f"Multiple cores detected, setting CPU_LEVEL to {"MULTPLE_CORES"}")
        CPU_LEVEL = "MULTIPLE_CORES"

    return True


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

producer.init_transactions()

def SendBackgroundStates(payload: list[main_dc.EnginePayload, main_dc.PerfPayload]):

    producer.begin_transaction()
    sent_state_data = producer.send('UNOBSERVED', payload)
    producer.commit_transaction()

    return sent_state_data

def SendMainStates(payload: list[main_dc.EnginePayload, main_dc.PerfPayload]):

    producer.begin_transaction()
    sent_state_data = producer.send('OBSERVED', payload)
    producer.commit_transaction()

    return sent_state_data

def SendMiscStates(payload: list[main_dc.EnginePayload, main_dc.PerfPayload]):

    producer.begin_transaction()
    sent_state_data = producer.send('MISC', payload)
    producer.commit_transaction()

    return sent_state_data
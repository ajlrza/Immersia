from engine.engine_dataclasses import main_dc
import asyncio

# NATIVE MODULES - OS-LEVEL
import threading, os, multiprocessing

HARDWARE_PRIORITY = {
    "0.85": 0.85,
    "0.70": 0.70,
    "0.50": 0.50
}

# Might use NamedTuples 
state_partitions: dict[str, list[StatePartition] | StatePartition]
state_queue: asyncio.Queue = asyncio.Queue()

def CreateStatePartition(partition_name: str, partition_count: int = 0) -> None:
    
    if (partition_count != 0):
        state_partitions[partition_name] = []

        for n in range(partition_count):
            state_partitions[partition_name].append([f"{partition_name} {n}"]) = None
    
    state_partitions.append(partition_name)

CPU_LEVELS: set[str] = ["ONE_CORE", "MULTIPLE_CORES"]

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


class Producer():

    __slots__=('')

    def __init__():
        pass

    async def send(partition_name, data):
        added_to_queue = await state_queue.put(state_partitions[partition_name].append(data))


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

produce = Producer()

def SendMainStates(payload: list[main_dc.EnginePayload, main_dc.PerfPayload]):

    sent_state_data = produce.send('OBSERVED', payload)
    produce.commit_transaction()

    return sent_state_data

def SendBackgroundStates(payload: list[main_dc.EnginePayload, main_dc.PerfPayload]):

    sent_state_data = produce.send('UNOBSERVED', payload)
    produce.commit_transaction()

    return sent_state_data

def SendMiscStates(payload: list[main_dc.EnginePayload, main_dc.PerfPayload]):

    sent_state_data = produce.send('MISC', payload)
    produce.commit_transaction()

    return sent_state_data
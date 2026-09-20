from fastapi import FastAPI, WebSocket
from kafka import KafkaConsumer, KafkaProducer
from kafka.structs import TopicPartition
from engine_dataclasses.main_dc import (
    EnginePayload,
    PromptPayload,
    PerfPayload,
    Data
)
from engine.llm_router import router

app = FastAPI()

OBSERVED = TopicPartition('OBSERVED', 0)
UNOBSERVED = TopicPartition('UNOBSERVED', 0)
MISC = TopicPartition('MISC', 0)

producer = KafkaProducer(bootstrap_servers='localhost:9092')

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')

consumer.assign([OBSERVED, UNOBSERVED, MISC])
consumer.poll

@app.get("/")

def read_root():
    return {"message": "Hello World"}

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

HARDWARE_PRIORITY = {
    "0.85": 0.85,
    "0.70": 0.70,
    "0.50": 0.50
}

@app.get("/engine", tags=["Engine"])
async def route_payloads(UserStates: EnginePayload = None, FirstPrompt: PromptPayload = None, PerfPayload: PerfPayload = None):
    
    if (FirstPrompt):
        Router = router.RouterEntrypoint(FirstPrompt)

        if Router:
            pass

    payload_bytes: bytes | None

    if (PerfPayload and PerfPayload.Data != ""):
        payload_bytes = PerfPayload.Data.encode('utf-8')
    else:
        payload_bytes = None
        print("No data received from performance payload.")

    if str(PerfPayload.PercUsed) in HARDWARE_PRIORITY:
        hardware_used = HARDWARE_PRIORITY[str(PerfPayload.PercUsed)]
        match hardware_used:
            case 0.85:
                producer.send('UNOBSERVED', value=payload_bytes, partition=0)
            case 0.70:
                producer.send('UNOBSERVED', value=payload_bytes, partition=0)
            case 0.50:
                producer.send('OBSERVED', value=payload_bytes, partition=0)
    else:
        producer.send('MISC', value=payload_bytes, partition=0)     

    if (UserStates):
        Router = router.RouterEntrypoint(UserStates)

        if Router:
            pass
        
        
    return {"status": "Payload routed successfully"}
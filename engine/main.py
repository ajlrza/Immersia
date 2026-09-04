from fastapi import FastAPI, WebSocket

from kafka import KafkaConsumer, KafkaProducer

from kafka.structs import TopicPartition

class PerfPayload(BaseModel):
    resources: float
    data: str  

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

@app.get("/engine", tags=["Engine"])
async def route_payloads(perfPayload: PerfPayload):
    
    hardware_priority = {
        "0.85": 0.85,
        "0.70": 0.70,
        "0.50": 0.50
    }

    payload_bytes = perfPayload.data.encode('utf-8')

    if str(perfPayload.resources) in hardware_priority:
        hardware_used = hardware_priority[str(perfPayload.resources)]
        
        match hardware_used:
            case 0.85:
                producer.send('UNOBSERVED', value=payload_bytes, partition=0)
            case 0.70:
                producer.send('UNOBSERVED', value=payload_bytes, partition=0)
            case 0.50:
                producer.send('OBSERVED', value=payload_bytes, partition=0)
    else:
        producer.send('MISC', value=payload_bytes, partition=0)  
        
    return {"status": "Payload routed successfully"}
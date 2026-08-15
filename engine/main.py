from fastapi import FastAPI, WebSocket
from kafka import KafkaConsumer

app = FastAPI()
socket = WebSocket()
consumer = KafkaConsumer()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Basic health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

@app.get("/engine", tags=["Engine"])
async def route_payloads():

    payload_priority = {
        "OBSERVED": 1,
        "UNOBSERVED": 0
    }

    hardware_priority = {
        "freeMem": 
    }

    observance_one = {}
    observance_two = {}
    observance_three = {}

    consumer.assign([observance_one, observance_two, observance_three])
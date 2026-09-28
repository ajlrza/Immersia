# THIRD PARTY - SERVER/CONNECTIONS
from fastapi import FastAPI, WebSocket

# NATIVE MODULES - TYPES
from collections.abc import Buffer

# ENIGNE MODULES 
from engine_dataclasses import main_dc, lmdb_dc
from engine.llm_router import router
from engine.hypervisor import kafka

app = FastAPI()

@app.get("/")

def read_root():
    return {"message": "Hello World"}

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

HYPERVISOR = kafka

@app.get("/engine", tags=["Engine"])
async def route_payloads(
    UserStates: main_dc.EnginePayload = None, 
    FirstPrompt: main_dc.PromptPayload = None, 
    PerfPayload: main_dc.PerfPayload = None
    ):

    payload_router = router.Router(FirstPrompt) if FirstPrompt else router.Router(UserStates)

    payload_bytes: bytes | None

    if (PerfPayload and PerfPayload.Data != ""):
        payload_bytes = PerfPayload.Data.encode('utf-8')
    else:
        payload_bytes = None
        print("No data received from performance payload.")

    if isinstance(payload_bytes, Buffer) and str(PerfPayload.PercUsed) in HYPERVISOR.HARDWARE_PRIORITY:

        hardware_used = HYPERVISOR.HARDWARE_PRIORITY[str(PerfPayload.PercUsed)]

        match hardware_used:
            case 0.85:
                HYPERVISOR.producer.send('UNOBSERVED', value=payload_bytes, partition=0)
            case 0.70:
                HYPERVISOR.producer.send('UNOBSERVED', value=payload_bytes, partition=0)
            case 0.50:
                HYPERVISOR.producer.send('OBSERVED', value=payload_bytes, partition=0)
    else:
        HYPERVISOR.producer.send('MISC', value=[UserStates, PerfPayload.PercUsed], partition=0)     
        
        
    return {
            "success": True,
            "status_code": 200,
            "message": "Engine successfully processed payload.",
            "data": {
                "Action": payload_router.Action,
                "Avatar": payload_router.Avatar,
                "Position": payload_router.Position,
                "World": payload_router.World,
                "Metadata": payload_router.Metadata
            }
        }
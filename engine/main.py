# ENIGNE MODULES 
from engine.state_dataclasses import main_dc, lmdb_dc
from engine.llm_router import router
from engine.state_hypervisor import Hypervisor, DistributeLoad

hypervisor = Hypervisor()

async def route_payloads(UserStates: main_dc.EnginePayload = None, FirstPrompt: main_dc.PromptPayload = None, PerfPayload: main_dc.PerfPayload = None):

    payload_router = router.Router(FirstPrompt) if FirstPrompt else router.Router(UserStates)

    payload_bytes: bytes | None

    if (PerfPayload and PerfPayload.Data != ""):
        payload_bytes = PerfPayload.Data.encode('utf-8')
    else:
        payload_bytes = None
        print("No data received from performance payload.")

    HARDWARE_PRIORITY = {
        "0.85": 0.85,
        "0.70": 0.70,
        "0.50": 0.50
    }

    if isinstance(payload_bytes, Buffer) and str(PerfPayload.PercUsed) in HARDWARE_PRIORITY:

        hardware_used = HARDWARE_PRIORITY[str(PerfPayload.PercUsed)]
        
        
    return {
            "success": True,
            "status_code": 200,
            "message": "Engine successfully processed payload.",
            "data": {
                "Avatar": payload_router.Avatar,
                "Position": payload_router.Position,
                "World": payload_router.World,
                "Metadata": payload_router.Metadata
            }
        }
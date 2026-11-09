# ENIGNE MODULES 
from engine.state_dataclasses import main_dc, lmdb_dc
from engine.state_hypervisor import Hypervisor, DistributeLoad

hypervisor = Hypervisor()

async def route_payloads(UserStates: main_dc.EnginePayload = None, FirstPrompt: main_dc.PromptPayload = None, PerfPayload: main_dc.PerfPayload = None):        
        
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
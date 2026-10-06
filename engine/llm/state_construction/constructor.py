from engine.engine_dataclasses import main_dc
from engine.db import db
import PIL.Image, re

PIL.ImageFile

# An assembler 
def overall_state_assemble(new_payload: main_dc.EnginePayload, image_byte: str) -> main_dc.EnginePayload:

    graph_assembly_db = db.StartDB()

    if (graph_assembly_db):
        db.DB.DbWrite(new_payload)

    pass
# General State Components Assembly
def general_state_assemble(gen_state: main_dc.GeneralState):
    pass

# Avatar State Components Assembly
def avatar_state_assemble(avt_state: main_dc.AvatarState):
    pass

# Position State Components Assembly
def position_state_assemble(pst_state: main_dc.PositionState):
    pass

# World State Components Assembly
def world_state_assemble(world_state: main_dc.WorldState):
    pass

def setting_state_assemble(api_response: str) -> bool:

    with open("./logs/world.txt", "w", encoding="utf-8") as file:
        file.write(api_response)

    file.close()

    world_setting: dict[str, any]
    filter = "/^\s*\*?\*?\s*(\w+):\*?\*?\s*([\s\S]*?)(?=(?:^\s*\*?\*?\s*\w+:)|(?:^\s*\*\*|\z))/gm"
    
    capture_settings = re.match(api_response, filter)


    return True

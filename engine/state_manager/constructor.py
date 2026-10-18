from engine.engine_dataclasses import main_dc, lmdb_dc
from engine.db import db
import PIL.Image, re, types, typing

FILTER = "/^\s*\*?\*?\s*(\w+):\*?\*?\s*([\s\S]*?)(?=(?:^\s*\*?\*?\s*\w+:)|(?:^\s*\*\*|\z))/gm"
WORLD_LOGS_PATH = "/logs/"
GENSTATE_STORAGE_PATH = "/storage/genstate/"
AVTSTATE_STORAGE_PATH = "/storage/avtstate/"
PSTSTATE_STORAGE_PATH = "/storage/pst/"
WORLDSTATE_STORAGE_PATH = "/storage/world/"

# An assembler 
def overall_state_assemble(new_payload: main_dc.EnginePayload, image_byte: str) -> bool:

    graph_assembly_db = db.StartDB()

    if (graph_assembly_db):
        db.DB.DbWrite(new_payload)

    return True
# General State Components Assembly
def general_state_assemble(gen_state_text: str, metadata: lmdb_dc.InteractionMetadata):
    gen_states: dict[str, any] | None
    
    capture_settings = re.fullmatch(gen_state_text, FILTER)

    if (isinstance(capture_settings, types.NoneType)):

        return False

    avt_states: dict[str, str | any] = capture_settings.groupdict()

    # graph file soon
    with open(GENSTATE_STORAGE_PATH + f'{metadata.EventWhen}', "w", encoding="utf-8") as file:
        file.write(gen_states)
    file.close()

    return True

# Avatar State Components Assembly
def avatar_state_assemble(avt_state_text: str, metadata: lmdb_dc.InteractionMetadata):
    avt_states: dict[str, any] | None

    capture_settings = re.fullmatch(avt_state_text, FILTER)

    if (isinstance(capture_settings, types.NoneType)):

        return False

    avt_states: dict[str, str | any] = capture_settings.groupdict()

    # graph file soon
    with open(AVTSTATE_STORAGE_PATH + f'{metadata.EventWhen}', "w", encoding="utf-8") as file:
        file.write(avt_states)
    file.close()

    return True

# Position State Components Assembly
def position_state_assemble(pst_state_text: str, metadata: lmdb_dc.InteractionMetadata):
    
    pst_states: dict[str, any] | None
    
    capture_settings = re.fullmatch(pst_state_text, FILTER)

    if (isinstance(capture_settings, types.NoneType)):

        return False

    pst_states: dict[str, str | any] = capture_settings.groupdict()

    # graph file soon
    with open(PSTSTATE_STORAGE_PATH + f'{metadata.EventWhen}', "w", encoding="utf-8") as file:
        file.write(pst_states)
    file.close()

    return True


# World State Components Assembly
def world_state_assemble(world_state_text: str, metadata: lmdb_dc.InteractionMetadata):

    world_setting: dict[str, any] | None
    
    capture_settings = re.fullmatch(world_state_text, FILTER)

    if (isinstance(capture_settings, types.NoneType)):

        with open(WORLD_LOGS_PATH, "w", encoding="utf-8") as file:
            file.write(world_state_text)
        file.close()

        return False

    world_setting: dict[str, str | any] = capture_settings.groupdict()

    with open(WORLDSTATE_STORAGE_PATH + f'{metadata.EventWhen}', "a", encoding="utf-8") as file:
        file.write(world_state_text)
    file.close()

    # graph file soon
    with open("./world/world_state.txt", "w", encoding="utf-8") as file:
        file.write(world_setting)
    file.close()

    return True

def setting_state_assemble(api_response: str, metadata: lmdb_dc.InteractionMetadata) -> bool:

    world_setting: dict[str, any] | None
    
    capture_settings = re.fullmatch(api_response, FILTER)

    if (isinstance(capture_settings, types.NoneType)):

        with open("./logs/world.txt", "w", encoding="utf-8") as file:
            file.write(api_response)
        file.close()

        return False

    world_setting: dict[str, str | any] = capture_settings.groupdict()

    with open(WORLD_LOGS_PATH + f'{metadata.EventWhen}', "w", encoding="utf-8") as file:
        file.write(api_response)
    file.close()

    # graph file soon
    with open("./world/root_world.txt", "w", encoding="utf-8") as file:
        file.write(world_setting)
    file.close()

    return True

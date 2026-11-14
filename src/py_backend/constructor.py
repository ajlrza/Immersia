from engine.engine_dataclasses import main_dc, lmdb_dc
from engine.db import db
import PIL, re, types, typing, io, base64

FILTER = "/^\s*\*?\*?\s*(\w+):\*?\*?\s*([\s\S]*?)(?=(?:^\s*\*?\*?\s*\w+:)|(?:^\s*\*\*|\z))/gm"
WORLD_LOGS_PATH = "/logs/"
GENSTATE_STORAGE_PATH = "/storage/genstate/"
AVTSTATE_STORAGE_PATH = "/storage/avtstate/"
PSTSTATE_STORAGE_PATH = "/storage/pst/"
WORLDSTATE_STORAGE_PATH = "/storage/world/"

def StateWriter(
    state: str, 
    state_text: str, 
    state_image: PIL.PngImagePlugin.PngImageFile, 
    state_image_tags: str, 
    metadata: lmdb_dc.InteractionMetadata):

    capture_settings = re.fullmatch(state_text, FILTER)

    if (isinstance(capture_settings, types.NoneType)):
        return False

    states: dict[str, str | any] = capture_settings.groupdict()

    byte_stream = io.BytesIO()
    state_image.save(byte_stream, format="PNG")
    png_bytes = byte_stream.getvalue()
    encoded_png = base64.b64encode(png_bytes).decode('utf-8')

    image_pointer: str = f"IMAGE={encoded_png}"
    image_tags_pointer: str = f"IMAGE_TAGS={state_image_tags}"

    match (state):
        case "gen":
            with open(GENSTATE_STORAGE_PATH + f'{metadata.EventWhen}', "w", encoding="utf-8") as file:
                file.write(state_text)

                file.write(image_tags_pointer)
                file.write(image_pointer)

                file.close()

        case "avt":
            with open(AVTSTATE_STORAGE_PATH + f'{metadata.EventWhen}', "w", encoding="utf-8") as file:
                file.write(state_text)

                file.write(image_tags_pointer)
                file.write(image_pointer)

                file.close()

        case "pst":
            with open(PSTSTATE_STORAGE_PATH + f'{metadata.EventWhen}', "w", encoding="utf-8") as file:
                file.write(state_text)

                file.write(image_tags_pointer)
                file.write(image_pointer)

                file.close()
                
        case "world":

            with open(WORLD_LOGS_PATH, "w", encoding="utf-8") as file:
                    file.write(state_text)
                    file.close()

            with open(WORLDSTATE_STORAGE_PATH + f'{metadata.EventWhen}', "w", encoding="utf-8") as file:
                file.write(state_text)

                file.write(image_tags_pointer)
                file.write(image_pointer)

                file.close()

    return True

# CONTEXT ASSEMBLERS TO FEED LLM IN GENERATING STATES
# USES B-TREE DATA STRUCTURE

database = db.KVDatabase()

# Each state assemblers may be invoked according to the resulting interactions and request
# of the tree IDs. The states are also assembled to maintain persistency.
# For instance, a user's recent state change may contain a tree ID that is relevant to it
# hence the state assembler would be invoked accordingly and the results are passed on
# to the LLM to inject contextual reasoning. But for the recent state change to contain
# a tree ID, it would require a graph math.

def general_state_assemble(tree_id: int | list[int]):
    '''
        Assembles general states according to requested tree ID.
        Contains non-specialized states that the user's digital word
        require.
    '''

def avatar_state_assemble(tree_id: int | list[int]):
    '''
        Assembles avatar states according to requested tree ID.
        Contains user's internal states that govern their own character
        n the digital world.
    '''

def position_state_assemble(tree_id: int | list[int]):
    '''
        Assembles positional states according to requested tree ID.
        Contains description of spatial address of characters in the 
        digital world.
    '''


# World State Components Assembly
def world_state_assemble(tree_id: int | list[int]):
    '''
        Assembles world states accroding to requested tree ID.
        Contains macro-level / high-level world event states 
        that drives the overall digital world's state. 
    '''



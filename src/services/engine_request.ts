import type { spriteProperties, loadEngineAPIKey, promptPayload, enginePayload } from '../interfaces/engine_interfaces'
import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../types/state_types'
import type { generalState, avatarState, positionState, worldState } from '../types/state_types'
import type { extValid } from '../types/data_validation_types'
import type { extPayload } from '../types/state_types'
import { checkMainStates, checkExtRecord, checkExtSingle } from '../services/validate_data'

    // need to strip whitespaces in both prompt payloads and engine payloads

const inMemoryBuffer: Record<string, any> = {
    rendering: Uint8Array ?? undefined, 
    stateProcess: Array ?? undefined,
};

const TTL: number = 0;
const SENT_COUNT: number = 0;
const BUFFER_COUNT: number = 0;
const ENGINE_STATUS: string = "UP";

export function validateData(payload: enginePayload): Record<string, Record<string, any>> {

    const statesValid: Record<string, Record<string, any>> = checkMainStates(payload)

    return statesValid;
};

export function validateExtRec(payload: extPayload | undefined): boolean | Record<string, extValid> {

    const extValidated: boolean | Record<string, extValid> = checkExtRecord(payload)

    return extValidated;
}

export function validateSingleExt(extState: generalStateExt | avatarStateExt | positionStateExt | worldStateExt): boolean | Record<string, boolean> {

    const extValidated: boolean | Record<string, boolean> = checkExtSingle(extState)

    return extValidated
}

export function sendEngineRequest(payload: enginePayload): any {

    let userStatesRequest: string

    const statesValidation: Record<string, any> = validateData(payload)
    let extValidation: boolean | Record<string, Record<string, any>> | Record<string, boolean>;

    if (payload.Ext) {

        switch (payload.Ext?.type) {
            case "generalState":
                extValidation = validateSingleExt(payload.Ext);
                break
            case "avatarState":
                extValidation = validateSingleExt(payload.Ext);
                break
            case "positionState":
                extValidation = validateSingleExt(payload.Ext);
                break
            case "worldState":
                extValidation = validateSingleExt(payload.Ext);
                break
            case "extRecord":
                extValidation = validateExtRec(payload.ExtRec)
        }
        userStatesRequest = 
        `
        Action: ${payload.Action}, 
        Avatar: ${payload.Avatar}, 
        State: ${payload.State}, 
        World: ${payload.World},
        Ext: ${payload.Ext}
        `
    } 
    else {
        extValidation = false
    }

    const userStates: string = `Action: ${payload.Action}, Avatar: ${payload.Avatar}, State: ${payload.State}, World: ${payload.World}`

    const socket: WebSocket = new WebSocket("https://www.immersia");
    let response;

    socket.addEventListener("message", (event) => {
        if (event.data) {
            response = event.data
        }
    })

    if (socket.readyState == 1) {
        socket.send(userStates.)
    } else {
        console.error("Websocket not ready.")
    }

    socket.close()

    return response;

};

export function processPromptWorld(payload: promptPayload, key: string, model: string): any {

    const clientPrompt: string = `Prompt: ${payload.prompt}, Metadata: ${payload.metadata}, Key: ${key}, Model: ${model}`

    const socket: WebSocket = new WebSocket("https://www.immersia");
    let response;

    socket.addEventListener("message", (event) => {
        if (event.data) {
            response = event.data
        }
    })

    if (socket.readyState == 1) {
        socket.send(clientPrompt)
    } else {
        console.error("Websocket not ready.")
    }

    socket.close()

    return response;
};
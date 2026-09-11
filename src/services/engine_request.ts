import type { spriteProperties, loadEngineAPIKey, promptPayload, enginePayload } from '../interfaces/engine_interfaces'
import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../types/state_types'
import type { extValidationRecord } from '../types/data_validation_types'
import { checkExtData, checkMainStates } from '../services/validate_data'

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

export function validateExt(
    extPayload: extValidationRecord | generalStateExt | avatarStateExt | positionStateExt | worldStateExt
): Record<string, Record<string, any>> {
    
    const extValid: Record<string, Record<string, any>> = checkExtData(extPayload)

    return extValid;
}

export function sendEngineRequest(payload: enginePayload): any {

    let userStatesRequest: string

    const statesValidation: Record<string, any> = validateData(payload)
    let extValidation: Record<string, Record<string, any>> | undefined;

    if (payload.Ext) {
        extValidation = validateExt(payload.Ext)
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
        extValidation = undefined
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
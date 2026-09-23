import type { extPayload } from '../types/state_types'
import type { extValid } from '../types/data_validation_types'
import { checkMainStates, checkExtRecord, checkExtSingle } from '../services/validate_data'
import type { generalState, avatarState, positionState, worldState } from '../types/state_types'
import type { spriteProperties, promptPayload, enginePayload } from '../interfaces/engine_interfaces'
import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../types/state_types'

// need to strip whitespaces in both prompt payloads and engine payloads

const SOCKET: WebSocket = new WebSocket("https://www.immersia");
const TTL: number = 180;

let sentCount: number = 0;
let bufferCount: number = 0;
let engineStatus: string = "UP";

let inMemoryBuffer: Record<string, any> = {
    rendering: Uint8Array ?? undefined, 
    stateProcess: Array ?? undefined,
};

export function closeSocket(): boolean {

    SOCKET.close()

    if (SOCKET.CLOSED) {
        return true
    }

    return false
}

export function validateData(payload: enginePayload): Record<string, Record<string, any>> {

    const statesValid: Record<string, Record<string, any>> = checkMainStates(payload)

    return statesValid;
};

export function validateExtRec(payload: extPayload | undefined): boolean | Record<string, extValid> {

    const extValidated: boolean | Record<string, extValid> = checkExtRecord(payload)

    return extValidated;
}

export function validateSingleExt(payload: enginePayload): boolean | Record<string, boolean> | Record<string, extValid> | undefined {

    let extValid: boolean | Record<string, boolean> | Record<string, extValid> | undefined;

    switch (payload.Ext?.type) {
        case "generalState":
            extValid = checkExtSingle(payload.Ext);
            break
        case "avatarState":
            extValid = checkExtSingle(payload.Ext);
            break
        case "positionState":
            extValid = checkExtSingle(payload.Ext);
            break
        case "worldState":
            extValid = checkExtSingle(payload.Ext);
            break
        case "extRecord":
            extValid = validateExtRec(payload.ExtRec)
        }
    

    return extValid
}

export function sendEngineRequest(payload: enginePayload, close: boolean = false): any | Record<string, boolean> {

    if (close) {
        closeSocket();
        return;
    }

    let userStatesRequest: string | undefined
    let retryTimes: number = 3

    let statesValidated: Record<string, any> | undefined = validateData(payload)
    let extValidated: boolean | Record<string, Record<string, any>> | Record<string, boolean> | undefined;

    if (payload.Ext) {
        extValidated = validateSingleExt(payload);
    } 
    else {
        extValidated = undefined
    }
    
    if (typeof statesValidated == 'object' && typeof extValidated == 'boolean' && !extValidated) {
        userStatesRequest = 
        `
        Action: ${payload.Action}, 
        Avatar: ${payload.Avatar}, 
        State: ${payload.State}, 
        World: ${payload.World},
        Ext: ${payload.Ext}
        `
    } else {

        console.log("No user states request detected, retrying...");
        
        while (typeof userStatesRequest != 'undefined' && typeof userStatesRequest == 'string') {

            if (retryTimes == 0) {

                statesValidated = undefined
                extValidated = undefined
                
                break
            }

            statesValidated = validateData(payload)
            extValidated = validateSingleExt(payload)

            retryTimes -= 1

        }
    }

    if (typeof statesValidated == 'undefined' && typeof userStatesRequest == 'undefined') {

        return {
            "Data": undefined, 
            "Success": false, 
            "Message": "Invalid Payload",
            "Log": {
                "statesValidated": statesValidated,
                "extValidated": extValidated
            }
        }

    }

    if (SOCKET.readyState == 1) {

        if (typeof userStatesRequest != 'undefined' && typeof userStatesRequest == 'string') {
            SOCKET.send(userStatesRequest)
            sentCount += 1
        }

    } else {
        console.error("Websocket not ready.")
    }

    let response;

    SOCKET.addEventListener("message", (event) => {

        setTimeout(() => {
            return "Connection Timeout";
        }, 18000);
        
        if (event.data) {
            response = event.data
        }
    })

    return response;

};

export function processPromptWorld(payload: promptPayload, key: string, model: string): any {

    // Future retry mechanism and data validation for first prompt
    let firstPromptRequest: string | undefined;
    let retryTimes: number = 3

    let promptValidated: Record<string, any> | undefined;


    const clientPrompt: string = `Prompt: ${payload.prompt}, Metadata: ${payload.metadata}, Key: ${key}, Model: ${model}`

    if (SOCKET.readyState == 1) {
        SOCKET.send(clientPrompt)
        sentCount += 1
    } else {
        console.error("Websocket not ready.")
    }

    let response;

    SOCKET.addEventListener("message", (event) => {

        setTimeout(() => {
            return "Connection Timeout";
        }, 18000);
        
        if (event.data) {
            response = event.data
        }
    })

    return response;
};
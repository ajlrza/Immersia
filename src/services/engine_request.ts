import type { actionList, userAction, spriteProperties, loadEngineAPIKey, createEngineRequest } from '../interfaces/engine_interfaces'

const action: userAction

interface clientPayload {
    metadata: object,
    prompt: string
}

export interface dataHashing {
   hashedObject: any,
   hashString: string // random
}

const inMemoryBuffer: object = {
    rendering: Uint8Array, 
    stateProcess: Array,
};

export function sendEngineRequest(payload: object): void {
    action.actionMade = payload.Action // javascript when an event triggered
    action.avatarState = payload.Avatar // already established, filled object in the frontendclient?
    action.generalState = payload.State // general
    action.worldState = payload.World
};

export function processPromptWorld(payload: clientPayload): any {

    const ws: WebSocket = new WebSocket("https://www.immersia.backend.cloudflare.com");
    ws.OPEN
    ws.send(payload.prompt)

    return ws.onmessage;

}



import type { actionList, userAction, spriteProperties, loadEngineAPIKey, enginePayload } from '../interfaces/engine_interfaces'

var action: userAction;

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

export function sendEngineRequest(payload: enginePayload): void {
    action.actionMade = payload.userAction.actionMade // javascript when an event triggered
    action.avatarState = payload.userAction.avatarState // already established, filled object in the frontendclient?
    action.generalState = payload.userAction.generalState // general
    action.worldState = payload.userAction.worldState
};

export function processPromptWorld(payload: clientPayload): any {

    const ws: WebSocket = new WebSocket("https://www.immersia.backend.cloudflare.com");
    let response;

    if (ws.readyState == 1) {
        ws.send(payload.prompt)
    } else {
        console.error("Websocket not ready.")
    }

    response = ws.onmessage ?? "";
    ws.close()

    return response;

}



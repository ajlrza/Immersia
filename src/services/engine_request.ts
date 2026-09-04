import type { spriteProperties, loadEngineAPIKey, clientPayload, enginePayload } from '../interfaces/engine_interfaces'

const inMemoryBuffer: object = {
    rendering: Uint8Array, 
    stateProcess: Array,
};

export function sendEngineRequest(payload: enginePayload): any {

    const userStates: string = `Action: ${payload.Action}, Avatar: ${payload.Avatar}, State: ${payload.State}, World: ${payload.World}`

    const socket: WebSocket = new WebSocket("https://www.immersia");
    let response;

    socket.addEventListener("message", (event) => {
        if (event.data) {
            response = event.data
        }
    })

    if (socket.readyState == 1) {
        socket.send(userStates)
    } else {
        console.error("Websocket not ready.")
    }

    socket.close()

    return response;

};

export function processPromptWorld(payload: clientPayload, key: string, model: string): any {

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

}



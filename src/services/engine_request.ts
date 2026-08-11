import { actionList, userAction, spriteProperties, loadEngineAPIKey, createEngineRequest } from '../interfaces/engine_interfaces'

export interface dataHashing {
   hashedObject: any,
   hashString: string // random
}

const inMemoryBuffer = {
    rendering: bytearray = [], 
    stateProcess: array = [],
}

const sendRequest(payload: object): void {
    const action: userAction
    action.actionMade = payload.Action // javascript when an event triggered
    action.avatarState = payload.Avatar // already established, filled object in the frontendclient?
    action.generalState = payload.State // general
    action.worldState = payload.World
}




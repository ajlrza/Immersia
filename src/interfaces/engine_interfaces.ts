import type { generalState, avatarState, positionState, worldState } from '../types/state_types'
import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../types/state_types'

export interface enginePayload {
    Action: actionList,
    Avatar: avatarState,
    State: generalState,
    Position: positionState,
    World: worldState
}

export interface clientPayload {
    metadata: object,
    prompt: string
}

export interface dataHashing {
   hashedObject: any,
   hashString: string // random
}

export interface actionList {
    isTouched: boolean,
    isMoved: boolean,
    isTalked: boolean
}

export interface userAction {
    actionMade: actionList
    generalState: generalState | null,
    avatarState: avatarState | null,
    avatarPosition: positionState | null,
    worldState: worldState | null
}

export interface spriteProperties {
    spriteName: string,
    spriteType: string,
    spriteImage: string
}

export interface loadEngineAPIKey {
    apiKey: string,
    modelName: string
}

export interface enginePayload {
    username: string,
    userAction: userAction,
    datetime: string
}

export interface extData {
    genExt: generalStateExt,
    avtExt: avatarStateExt,
    pstExt: positionStateExt,
    wrldExt: worldStateExt
}

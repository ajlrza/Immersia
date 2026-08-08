import type { generalState, avatarState, avatarPositionState, worldState } from '../types/state_types'

export interface actionList {
    isTouched: boolean,
    isMoved: boolean,
    isTalked: boolean
}

export interface userAction {
    actionMade: actionList
    generalState: generalState | null,
    avatarState: avatarState | null,
    avatarPosition: avatarPositionState | null,
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

export interface createEngineRequest {
    username: string,
    userAction: userAction,
    datetime: string
}


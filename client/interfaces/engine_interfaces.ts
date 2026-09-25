import type { extPayload } from '../types/state_types'
import type { generalState, avatarState, positionState, worldState } from '../types/state_types'
import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../types/state_types'
import type { generalStateImage, avatarStateImage, positionStateImage, worldStateImage } from '../types/state_types'

export type enginePayload = {
  Action: actionList;
  Avatar: avatarState;
  State: generalState;
  Position: positionState;
  World: worldState;
  Ext?:
    | generalStateExt 
    | avatarStateExt 
    | positionStateExt 
    | worldStateExt;
  ExtRec?: 
    | extPayload
};

export type engineImages = {
    linkedPayload: enginePayload;
    general: generalStateImage;
    avatar: avatarStateImage;
    position: positionStateImage;
    world: worldStateImage;
}

// Stored in LMDB and read from LMDB then mapped to Graph DBs
export interface InteractionMetadata {
    EventWhen: Date
    GraphMasterID: number // Master identifier responsible for placing the interaction data
    GraphNodes: number // How many graph nodes, used for optimizing and storing properly
    StatesAffected: number // How many states affected, used also for optimizing and compress
    EngineStatus: number // Engine status as of this interaction
}

export interface GoResponse {
    NewStates: enginePayload
    NewImage: engineImages
}

export interface EngineResponse {
    Data: GoResponse | undefined
    Success: boolean
    Message: string
    Log: object
}

export interface promptPayload {
    metadata: object,
    prompt: string,
    key?: string,
    model?: string
}

export interface dataHashing {
   hashedObject: any,
   hashString: string 
}

export interface actionList {
    isTouched: boolean,
    isMoved: boolean,
    isTalked: boolean
}

export interface spriteProperties {
    spriteName: string,
    spriteType: string,
    spriteImage: string
}
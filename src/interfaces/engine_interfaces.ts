import type { generalState, avatarState, positionState, worldState } from '../types/state_types'
import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../types/state_types'

export type enginePayload = {
  Action: actionList;
  Avatar: avatarState;
  State: generalState;
  Position: positionState;
  World: worldState;
  Ext?: 
    | Record<string, generalStateExt & avatarStateExt & positionStateExt & worldStateExt> 
    | generalStateExt 
    | avatarStateExt 
    | positionStateExt 
    | worldStateExt;
};

export interface promptPayload {
    metadata: object,
    prompt: string
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

export interface loadEngineAPIKey {
    apiKey: string,
    modelName: string
}

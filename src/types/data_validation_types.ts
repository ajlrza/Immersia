import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../types/state_types'
import type { generalState, avatarState, positionState, worldState } from '../types/state_types'

export type definedMainList = [
    generalState | undefined,
    avatarState | undefined,
    positionState | undefined,
    worldState | undefined
]

export type definedLinkerList = [
    generalState | undefined,
    avatarState | undefined,
    positionState | undefined,
    worldState | undefined
]

export type definedExtList = [
    generalStateExt | undefined, 
    avatarStateExt | undefined, 
    positionStateExt | undefined, 
    worldStateExt | undefined,
]

export type mainValid = {
    "gen": boolean,
    "avt": boolean,
    "pst": boolean,
    "world": boolean,
    "defined": definedMainList
}

export type linkerValid = {
    "genLinker": boolean,
    "avtLinker": boolean,
    "pstLinker": boolean,
    "worldLinker": boolean,
    "defined": definedLinkerList
}

export type extValid = {
    "genExt": boolean,
    "avtExt": boolean,
    "pstExt": boolean,
    "worldExt": boolean
    "defined"?: definedExtList,
}

export type strStatesValid = {
    "gen": boolean,
    "avt": boolean,
}

export type numStatesValid = {
    "pst": boolean,
    "world": boolean
}

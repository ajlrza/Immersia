// Generalized, Localized, and Deterministic Types

export type generalState = {
    StateLinker: generalState
    StateOne: string,
    StateTwo: string,
    StateThree: string
};

export type avatarState = {
    StateLinker: avatarState
    EmotionOne: string,
    EmotionTwo: string,
    EmotionThree: string
}

export type positionState = {
    StateLinker: positionState,
    x: number,
    y: number,
    z: number
}

export type worldState = {
    StateLinker: worldState,
    Gravity: number,
    Force: number,
    Torque: number,
    Mass: number,
    Acceleration: number
}

// Intuitive, Semantic, and Imaginative Types

export type extPayload = {
    genExt: generalStateExt,
    avtExt: avatarStateExt,
    pstExt: positionStateExt,
    worldExt: worldStateExt
}

export type extStates = {
  Ext: generalState | avatarState | positionState | worldState
};

export type generalStateExt = {
    generalState: generalState,
    extStates: Record<string, any>;
}

export type avatarStateExt = {
    avatarState: avatarState,
    extStates: Record<string, any>;
}

export type positionStateExt = {
    positionState: positionState,
    extStates: Record<string, any>;
}

export type worldStateExt = {
    worldState: worldState,
    extStates: Record<string, any>;
}
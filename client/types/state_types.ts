// Generalized, Localized, and Deterministic Types

export type PixelData = { 
  width: number; 
  height: number; 
  pixels: number[]; 
  z_buffer?: number;
  channel?: number;
};

export type generalState = {
    StateLinker: generalState
    StateOne: string,
    StateTwo: string,
    StateThree: string
};


export type generalStateImage = {
    image: PixelData[]
}

export type avatarState = {
    StateLinker: avatarState
    EmotionOne: string,
    EmotionTwo: string,
    EmotionThree: string
}

export type avatarStateImage = {
    image: PixelData[]
}

export type positionState = {
    StateLinker: positionState,
    x: number,
    y: number,
    z: number
}

export type positionStateImage = {
    image: PixelData[]
}

export type worldState = {
    StateLinker: worldState,
    Gravity: number,
    Force: number,
    Torque: number,
    Mass: number,
    Acceleration: number
}

export type worldStateImage = {
    image: PixelData[]
}

// Intuitive, Semantic, and Imaginative Types

export type extPayload = {
    type: string
    genExt: generalStateExt,
    avtExt: avatarStateExt,
    pstExt: positionStateExt,
    worldExt: worldStateExt
}

export type extStates = {
  Ext: generalState | avatarState | positionState | worldState
};

export type generalStateExt = {
    type: string,
    extStates: Record<string, any>;
}

export type avatarStateExt = {
    type: string,
    extStates: Record<string, any>;
}

export type positionStateExt = {
    type: string,
    extStates: Record<string, any>;
}

export type worldStateExt = {
    type: string,
    extStates: Record<string, any>;
}
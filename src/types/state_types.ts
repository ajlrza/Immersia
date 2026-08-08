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

export type avatarPositionState = {
    StateLinker: avatarPositionState,
    x: string,
    y: string,
    z: string
}

export type worldState = {
    StateLinker: worldState,
    Gravity: number,
    Force: number,
    Torque: number,
    Mass: number,
    Acceleration: number
}

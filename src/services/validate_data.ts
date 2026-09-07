import type { actionList, spriteProperties, loadEngineAPIKey, enginePayload } from '../interfaces/engine_interfaces'
import type { generalState, avatarState, positionState, worldState } from '../types/state_types'
import type { extData } from '../interfaces/engine_interfaces'

type Validator = { validate: (val: unknown) => boolean };

class StringValidator {
  validate(val: unknown): boolean {
    return typeof val === "string";
  }
}

class BooleanValidator {
  validate(val: unknown): boolean {
    return typeof val === "boolean";
  }
}

class ObjectValidator {
    validate(val: unknown): boolean {
        return typeof val === "object";
    }
}

const nullableValidator = (inner: Validator): Validator => ({
  validate: (val) => val === null || inner.validate(val)
});


const genStateValid: object = {
    stateLinkerValid: 
}

function validateExtData(extData: extData): void {
        const genExt: any = extData.genExt;
        const avtExt: any = extData.avtExt;
        const pstExt: any = extData.pstExt;
        const wrldExt: any = extData.wrldExt
};

function validateActionData(actionData: actionList): void {
        const movedData: any = actionData.isMoved;
        const talkData: any = actionData.isTalked;
        const touchData: any = actionData.isTouched;
};

const objValidate = new ObjectValidator()
const strValidate = new StringValidator()
const boolValidate = new BooleanValidator()

function checkExtData(obj: any): boolean | Record<string, boolean> {
    
    let invalidCount: number = 0;

    if (!obj || typeof obj !== 'object')  {  
        invalidCount += 1;
    }

    if (!('genExt' in obj != undefined) && !('avtExt' in obj != undefined) && ('pstExt' in obj != undefined) && ('wrldExt' in obj != undefined)) {
        invalidCount += 4;
    }

    const extValidated: Record<string, boolean> = {
        objectOrNot: 
            objValidate.validate(obj.genExt.generalState) && objValidate.validate(obj.genExt.avatarState) && 
            objValidate.validate(obj.genExt.positionState) && objValidate.validate(obj.genExt.worldState),

        stringOrNot: 
            strValidate.validate(obj.genExt.generalState.StateOne) && strValidate.validate(obj.genExt.generalState.StateTwo) && strValidate.validate(obj.genExt.generalState.StateThree) &&
            strValidate.validate(obj.avtExt.avatarState.EmotionOne) && strValidate.validate(obj.avtExt.avatarState.EmotionTwo) && strValidate.validate(obj.avtExt.avatarState.EmotionThree) &&
            strValidate.validate(obj.pstExt.positionState.x) && strValidate.validate(obj.pstExt.positionState.y) && strValidate.validate(obj.pstExt.positionState.z),
    }

    return extValidated
}


function checkDataTypes(states: any): Record<string, any> {

    const genState: generalState = states ?? undefined;
    const avtState: avatarState = states ?? undefined;
    const pstState: positionState = states ?? undefined;
    const worldState: worldState = states ?? undefined;

    if (
        (typeof genState !== 'object' 
        || typeof avtState !== 'object'
        || typeof pstState !== 'object'
        || typeof worldState !== 'object') 
        || (genState === undefined
        || avtState === undefined
        || pstState === undefined
        || worldState === undefined)
    ) {return {"state": genState ?? avtState ?? pstState ?? worldState ?? undefined, "valid": false}};

    if (
        (typeof genState?.StateLinker !== 'object'  
        || typeof avtState?.StateLinker !== 'object'
        || typeof pstState?.StateLinker !== 'object'
        || typeof worldState?.StateLinker !== 'object') 
        || (genState?.StateLinker === undefined
        || avtState?.StateLinker === undefined
        || pstState?.StateLinker === undefined
        || worldState?.StateLinker === undefined)
    ) {return {"state": genState.StateLinker ?? avtState.StateLinker ?? pstState.StateLinker ?? worldState.StateLinker ?? undefined, "valid": false}};
    
    // Soon do others

    //!['light', 'dark'].includes(core.theme)

    return {}

}
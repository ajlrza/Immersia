import type { actionList, userAction, spriteProperties, loadEngineAPIKey, enginePayload } from '../interfaces/engine_interfaces'
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

class validateExtData {

    validateExtData(extData: extData): void {
        const genExt: any = extData.genExt;
        const avtExt: any = extData.avtExt;
        const pstExt: any = extData.pstExt;
        const wrldExt: any = extData.wrldExt;
    };

    checkExtData(obj: any) {

        let invalidCount: number = 0;

        const objValidate = new ObjectValidator()
        const strValidate = new StringValidator()
        const boolValidate = new BooleanValidator()

        if (!obj || typeof obj !== 'object') 
            invalidCount += 1;
        if (!('genExt' in obj != undefined) && !('avtExt' in obj != undefined) && ('pstExt' in obj != undefined) && ('wrldExt' in obj != undefined)) 
            invalidCount += 4;

        const validateData: object = {
            objectOrNot: objValidate.validate(obj.genExt.generalState) && objValidate.validate(obj.genExt.avatarState) && objValidate.validate(obj.genExt.positionState) &&
                objValidate.validate(obj.genExt.worldState),
            stringOrNot: strValidate.validate(obj.genExt.generalState.StateOne) && strValidate.validate(obj.genExt.generalState.StateTwo) && strValidate.validate(obj.genExt.generalState.StateThree) &&
                strValidate.validate(obj.avtExt.avatarState.EmotionOne) && strValidate.validate(obj.avtExt.avatarState.EmotionTwo) && strValidate.validate(obj.avtExt.avatarState.EmotionThree) &&
                strValidate.validate(obj.pstExt.positionState.x) && strValidate.validate(obj.pstExt.positionState.y) && strValidate.validate(obj.pstExt.positionState.z),
        }
        
        const core = obj.genExt.generalState;
        if (typeof core !== 'object' || core === null) return false;
        if (typeof core.StateLinker !== 'generalState') return false;
        if (typeof core.StateOne !== 'string' || core.StateTwo !== 'string' || core.StateThree !== 'string') return false;

        if (typeof obj.extStates !== 'object' || obj.extStates === null) return false;

        !['light', 'dark'].includes(core.theme)
    }
}
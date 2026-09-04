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

class validateData {

    valid() {
        
    }

    const invalidCount: number = 0;

    const objValidate = new ObjectValidator()
    const strValidate = new StringValidator()
    const boolValidate = new BooleanValidator()

    validateExtData(extData: extData): void {
        const genExt: any = extData.genExt;
        const avtExt: any = extData.avtExt;
        const pstExt: any = extData.pstExt;
        const wrldExt: any = extData.wrldExt
    };

    validateActionData(actionData: actionList): void {
        const movedData: any = actionData.isMoved;
        const talkData: any = actionData.isTalked;
        const touchData: any = actionData.isTouched;
    }

    checkExtData(obj: any): boolean | Record<string, boolean> {

        if (!obj || typeof obj !== 'object') 
            this.invalidCount += 1;

        if (!('genExt' in obj != undefined) && !('avtExt' in obj != undefined) && ('pstExt' in obj != undefined) && ('wrldExt' in obj != undefined)) 
            this.invalidCount += 4;

        const extValidated: Record<string, boolean> = {
            objectOrNot: 
                this.objValidate.validate(obj.genExt.generalState) && this.objValidate.validate(obj.genExt.avatarState) && 
                this.objValidate.validate(obj.genExt.positionState) && this.objValidate.validate(obj.genExt.worldState),

            stringOrNot: 
                this.strValidate.validate(obj.genExt.generalState.StateOne) && this.strValidate.validate(obj.genExt.generalState.StateTwo) && this.strValidate.validate(obj.genExt.generalState.StateThree) &&
                this.strValidate.validate(obj.avtExt.avatarState.EmotionOne) && this.strValidate.validate(obj.avtExt.avatarState.EmotionTwo) && this.strValidate.validate(obj.avtExt.avatarState.EmotionThree) &&
                this.strValidate.validate(obj.pstExt.positionState.x) && this.strValidate.validate(obj.pstExt.positionState.y) && this.strValidate.validate(obj.pstExt.positionState.z),
        }
     
        const core = obj.genExt.generalState;
        if (typeof core !== 'object' || core === null) return false;

        if (typeof core.StateLinker !== 'object') return false;

        if (typeof core.StateOne !== 'string' || core.StateTwo !== 'string' || core.StateThree !== 'string') return false;

        if (typeof obj.extStates !== 'object' || obj.extStates === null) return false;

        !['light', 'dark'].includes(core.theme)

        return extValidated;
    }
}
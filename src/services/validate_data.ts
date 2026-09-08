import type { actionList, spriteProperties, loadEngineAPIKey, enginePayload } from '../interfaces/engine_interfaces'
import type { generalState, avatarState, positionState, worldState } from '../types/state_types'
import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../types/state_types'

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
})

function checkActionData(actionData: actionList): void {
    const movedData: any = actionData.isMoved;
    const talkData: any = actionData.isTalked;
    const touchData: any = actionData.isTouched;
};

const objValidate = new ObjectValidator()
const strValidate = new StringValidator()
const boolValidate = new BooleanValidator()

function checkExtData(extData: any): Record<string, Record<string, any>> {
    
    let invalidCount: number = 0;

    const genExt: generalStateExt = extData ?? undefined;
    const avtExt: avatarStateExt = extData ?? undefined;
    const pstExt: positionStateExt = extData ?? undefined;
    const worldExt: worldStateExt = extData ?? undefined;

    if (!extData || typeof extData !== 'object')  {  
        invalidCount += 1;
    }

    if (!('extStates' in genExt === undefined) && !('extStates' in avtExt === undefined) && ('extStates' in pstExt === undefined) && ('extStates' in worldExt === undefined)) {
        invalidCount += 4;
    }

    const extObjValid: Record<string, any> = {
        "genExt": objValidate.validate(genExt),
        "avtExt": objValidate.validate(avtExt),
        "pstExt": objValidate.validate(pstExt), 
        "worldExt": objValidate.validate(worldExt), 
        "defined": [
            genExt ?? undefined,
            avtExt ?? undefined,
            pstExt ?? undefined,
            worldExt ?? undefined
        ]
    };

    // yo ill do the onefor extState its record<string, any> validation later, for now its extObj as a whole since
    // extData is mainData + extData record<string, any>

    return {
        "obj": extObjValid,
        "record": {} 
    }
}


function checkMainStates(states: any): Record<string, Record<string, any>> {

    const genState: generalState = states ?? undefined;
    const avtState: avatarState = states ?? undefined;
    const pstState: positionState = states ?? undefined;
    const worldState: worldState = states ?? undefined;

    const objValid: Record<string, any> = {
        "general": objValidate.validate(genState),
        "avatar": objValidate.validate(avtState),
        "position": objValidate.validate(pstState), 
        "world": objValidate.validate(worldState), 
        "defined": [
            genState ?? undefined,
            avtState ?? undefined,
            pstState ?? undefined,
            worldState ?? undefined
        ],
    }

    const linkerValid: Record<string, any> = {
        "genLinker": objValidate.validate(genState?.StateLinker),
        "avtLinker": objValidate.validate(avtState?.StateLinker),
        "pstLinker": objValidate.validate(pstState?.StateLinker),
        "worldLinker": objValidate.validate(worldState?.StateLinker),
        "defined": [
            genState.StateLinker ?? undefined,
            avtState.StateLinker ?? undefined,
            pstState.StateLinker ?? undefined,
            worldState.StateLinker ?? undefined
        ]
    }

    return {
        "obj": objValid,
        "linker": linkerValid
    }
    
};
    
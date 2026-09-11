import type { actionList, spriteProperties, loadEngineAPIKey, enginePayload } from '../interfaces/engine_interfaces'
import type { extStates, generalState, avatarState, positionState, worldState } from '../types/state_types'
import type { 
    extPayload, 
    generalStateExt, 
    avatarStateExt, 
    positionStateExt, 
    worldStateExt } from '../types/state_types'
import type { 
    mainValid, 
    linkerValid, 
    extValid, 
    definedExtList, 
    definedMainList, 
    strStatesValid, 
    numStatesValid } from '../types/data_validation_types'

type Validator = { validate: (val: unknown) => boolean };

class StringValidator {
  validate(val: unknown): boolean {
    return typeof val === "string";
  }
}

class NumValidator {
    validate(val: unknown): boolean {
        return typeof val === "number"
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

class RecordValidator {
    validate(val: unknown): boolean {
        return typeof val === 'object' && typeof val !== null && !Array.isArray(val)
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
const numValidate = new NumValidator()
const recValidate = new RecordValidator()
const boolValidate = new BooleanValidator()

export function checkMainStates(states: enginePayload): Record<string, mainValid | linkerValid | strStatesValid | numStatesValid> {

    const objValid: mainValid = {
        "gen": objValidate.validate(states.State),
        "avt": objValidate.validate(states.Avatar),
        "pst": objValidate.validate(states.Position), 
        "world": objValidate.validate(states.World), 
        "defined": [
            states.State ?? undefined,
            states.Avatar ?? undefined,
            states.Position ?? undefined,
            states.World ?? undefined
        ],
    }

    const strValid: strStatesValid = {
        "gen": strValidate.validate(states.State.StateOne) 
               && strValidate.validate(states.State.StateTwo) 
               && strValidate.validate(states.State.StateThree),
        "avt": strValidate.validate(states.Avatar.EmotionOne)
               && strValidate.validate(states.Avatar.EmotionTwo)
               && strValidate.validate(states.Avatar.EmotionThree),
    }

    const numValid: numStatesValid= {
        "pst": numValidate.validate(states.Position.x)
               && numValidate.validate(states.Position.y)
               && numValidate.validate(states.Position.z),
        "world": numValidate.validate(states.World.Acceleration)
                 && numValidate.validate(states.World.Force)
                 && numValidate.validate(states.World.Gravity)
                 && numValidate.validate(states.World.Mass)
                 && numValidate.validate(states.World.Torque)
    }

    const linkerValid: linkerValid = {
        "genLinker": objValidate.validate(states.State?.StateLinker),
        "avtLinker": objValidate.validate(states.Avatar?.StateLinker),
        "pstLinker": objValidate.validate(states.Position?.StateLinker),
        "worldLinker": objValidate.validate(states.World?.StateLinker),
        "defined": [
            states.State.StateLinker ?? undefined,
            states.Avatar.StateLinker ?? undefined,
            states.Position.StateLinker ?? undefined,
            states.World.StateLinker ?? undefined
        ]
    }

    return {
        "mainValidat": objValid,
        "linkerValid": linkerValid,
        "strValid": strValid,
        "numValid": numValid
    }
    
};

export function checkExtData(extData: extPayload): boolean | Record<string, extValid> {

    if (!extData || typeof extData !== 'object')  {  
        return false
    }

    const extObjValid: extValid = {
        "genExt": objValidate.validate(extData.genExt),
        "avtExt": objValidate.validate(extData.avtExt),
        "pstExt": objValidate.validate(extData.pstExt), 
        "worldExt": objValidate.validate(extData.worldExt), 
        "defined": [
            extData.genExt ?? undefined,
            extData.avtExt ?? undefined,
            extData.pstExt ?? undefined,
            extData.worldExt ?? undefined
        ]
    };

    const extRecordsValid: extValid = {
        "genExt": recValidate.validate(extData.genExt.extStates),
        "avtExt": recValidate.validate(extData.avtExt.extStates),
        "pstExt": recValidate.validate(extData.pstExt.extStates),
        "worldExt": recValidate.validate(extData.worldExt.extStates)
    }

    // yo ill do the onefor extState its record<string, any> validation later, for now its extObj as a whole since
    // extData is mainData + extData record<string, any>

    return {
        "extObj": extObjValid,
        "extRec": extRecordsValid
    }
}
    
import type { extPayload } from '../src/ts_model/state_types'
import type { extValid } from '../src/ts_model/data_validation_types'
import { checkMainStates, checkExtRecord, checkExtSingle } from './validate_data'
import type { generalState, avatarState, positionState, worldState } from '../src/ts_model/state_types'
import type { spriteProperties, promptPayload, enginePayload } from '../../interfaces/engine_interfaces'
import type { generalStateExt, avatarStateExt, positionStateExt, worldStateExt } from '../src/ts_model/state_types'

let sentCount: number = 0;

export function validateData(payload: enginePayload): Record<string, Record<string, any>> {

    const statesValid: Record<string, Record<string, any>> = checkMainStates(payload)

    return statesValid;
};

export function validateExtRec(payload: extPayload | undefined): boolean | Record<string, extValid> {

    const extValidated: boolean | Record<string, extValid> = checkExtRecord(payload)

    return extValidated;
}

export function validateSingleExt(payload: enginePayload): boolean | Record<string, boolean> | Record<string, extValid> | undefined {

    let extValid: boolean | Record<string, boolean> | Record<string, extValid> | undefined;

    switch (payload.Ext?.type) {
        case "generalState":
            extValid = checkExtSingle(payload.Ext);
            break
        case "avatarState":
            extValid = checkExtSingle(payload.Ext);
            break
        case "positionState":
            extValid = checkExtSingle(payload.Ext);
            break
        case "worldState":
            extValid = checkExtSingle(payload.Ext);
            break
        case "extRecord":
            extValid = validateExtRec(payload.ExtRec)
        }
    

    return extValid
}

export function sendEngineRequest(payload: enginePayload): any | Record<string, boolean> {


    let userStatesRequest: string | undefined
    let retryTimes: number = 3

    let statesValidated: Record<string, any> | undefined = validateData(payload)
    let extValidated: boolean | Record<string, Record<string, any>> | Record<string, boolean> | undefined;

    if (payload.Ext) {
        extValidated = validateSingleExt(payload);
    } 
    else {
        extValidated = undefined
    }
    
    if (typeof statesValidated == 'object' && typeof extValidated == 'boolean' && !extValidated) {
        userStatesRequest = 
        `
        Action: ${payload.Action}, 
        Avatar: ${payload.Avatar}, 
        State: ${payload.State}, 
        World: ${payload.World},
        Ext: ${payload.Ext}
        `
    } else {

        console.log("No user states request detected, retrying...");
        
        while (typeof userStatesRequest != 'undefined' && typeof userStatesRequest == 'string') {

            if (retryTimes == 0) {

                statesValidated = undefined
                extValidated = undefined
                
                break
            }

            statesValidated = validateData(payload)
            extValidated = validateSingleExt(payload)

            retryTimes -= 1

        }
    }

    if (typeof statesValidated == 'undefined' && typeof userStatesRequest == 'undefined') {

        return {
            "Data": undefined, 
            "Success": false, 
            "Message": "Invalid Payload",
            "Log": {
                "statesValidated": statesValidated,
                "extValidated": extValidated
            }
        }

    }

};
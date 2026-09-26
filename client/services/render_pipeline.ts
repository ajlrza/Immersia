import request
import type { engineImages, enginePayload } from '../interfaces/engine_interfaces'
import {startRender, resetCanvas } from '../services/render'
import type { generalStateImage, avatarStateImage, positionStateImage, worldStateImage } from '../types/state_types'

let wholeImg: engineImages | undefined;
let genStateImg: generalStateImage | undefined;
let avtStateImg: avatarStateImage | undefined;
let pstStateImg: positionStateImage | undefined;
let worldStateImg: worldStateImage | undefined;

type objResponse = {
    data: string | Uint8Array
}

function isBase64(str: string | Uint8Array): boolean {
  const base64Regex = /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/;

  return base64Regex.test(str);
}

async function Decode(response: objResponse) {
    if (isBase64(response?.data)) {

        const renderBytes = startRender(response?.data)
    } 
    else if (!(isBase64(response?.data)) && typeof response?.data == 'string') {
        
        const gotURLImg = await fetch(response?.data);
  
        if (!gotURLImg.ok) {
            throw new Error('Network response was not ok');
            // trigger loading animation
        }

    }
}


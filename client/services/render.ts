const width = 2;
const height = 2;

const pixels = new Uint8Array([

  255, 0, 0, 255, 
  
  0, 255, 0, 255, 
  
  0, 0, 255, 255, 
  
  255, 255, 255, 128
]);

const image: any = [width, height, pixels]

let buffer = new ArrayBuffer(8); 

export function renderOptimize(bytes: Uint8Array): Uint8Array {

    return bytes;
};

export function startRender(data: string): Uint8Array {

    if (typeof data != 'string') {
        return new Uint8Array()
    }

    let imgArray: any;
    const decodeImg64: string = atob(data);

    if (typeof data == 'string') {
        const checkBytes: RegExpMatchArray | null = decodeImg64.match("^[0-9]+$");

        if (checkBytes != null && checkBytes.length > 1) {
            imgArray = new Uint8Array(decodeImg64.length);
        }
    }
    
    for (let i = 0; i < decodeImg64.length; i++) {
        imgArray[i] = decodeImg64.charCodeAt(i);
    }

    return imgArray

};

export function resetCanvas(): Uint8Array {
    return new Uint8Array();
}

const width = 2;
const height = 2;

const pixels = new Uint8Array([

  255, 0, 0, 255, 
  
  0, 255, 0, 255, 
  
  0, 0, 255, 255, 
  
  255, 255, 255, 128
]);

const image: any = [width, height, pixels]

export function renderOptimize(bytes: Uint8Array): Uint8Array {

    return bytes;
};

export function startRender(): Uint8Array {
    const buffer = new ArrayBuffer(8); 
    const bytes = new Uint8Array(buffer);
    return bytes;
};

export function resetCanvas(): Uint8Array {
    const buffer = new ArrayBuffer(0)
    const bytes = new Uint8Array(buffer);
    return bytes;
}


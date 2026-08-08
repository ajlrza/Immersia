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

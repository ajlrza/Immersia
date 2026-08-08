from fastapi import FastAPI, WebSocket

app = FastAPI()
socket = WebSocket()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Basic health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}


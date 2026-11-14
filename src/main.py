from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import html

app = FastAPI()

def run_engine(action: str) -> dict:
    # placeholder: assemble context -> call LLM -> validate -> store
    return {"action": action, "emotion": "curious",
            "position": "(0, 0, 0)", "event": "The world is quiet."}

def page() -> str:
    rows = "".join(
        f"<li><b>{html.escape(h['action'])}</b><br>"
        f"Emotion: {html.escape(h['emotion'])} | "
        f"Position: {html.escape(h['position'])} | "
        f"World: {html.escape(h['event'])}</li>"
        for h in reversed(history)
    )
    return f"""<!doctype html>
<html><body style="font-family: monospace; max-width: 700px; margin: 2rem auto">
  <h1>World Engine</h1>
  <form method="post" action="/act">
    <input name="action" placeholder="What do you do?" autofocus required>
    <button>Go</button>
  </form>
  <ul>{rows}</ul>
</body></html>"""

@app.get("/", response_class=HTMLResponse)
def index():
    return page()

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class ActionIn(BaseModel):
    action: str

@app.post("/act")
def act(body: ActionIn):
    return run_engine(body.action)

# Serve index.html + compiled JS. Mount last so it doesn't shadow /act.
app.mount("/", StaticFiles(directory="web", html=True), name="web")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Mount static files (React build)
app.mount("/static", StaticFiles(directory="static/static"), name="static")

@app.get("/")
def serve_root():
    return FileResponse("static/index.html")

@app.get("/docs")
def get_docs_redirect():
    return FileResponse("static/index.html")  # Optional override for SPA routing

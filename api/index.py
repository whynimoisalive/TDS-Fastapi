from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
)

# Load marks data
with open(os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')) as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    marks = [int(entry["marks"]) for entry in marks_data if entry["name"] in name]
    return {"marks": marks}
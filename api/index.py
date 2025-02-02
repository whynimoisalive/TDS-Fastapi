import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so that GET requests from any origin are allowed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the student marks data at startup.
with open("q-vercel-python.json", "r") as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    """
    Expects one or more "name" query parameters.
    Example: /api?name=Alice&name=Bob
    Returns: { "marks": [95, 82] }
    If a name is not found, returns 0 as the mark.
    """
    return {"marks": [marks_data.get(n, 0) for n in name]}

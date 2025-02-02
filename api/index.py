import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI app
app = FastAPI()

# Enable CORS for all origins and GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the student marks JSON file once at startup
with open("q-vercel-python.json", "r") as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    """
    Given one or more query parameters 'name', return a JSON object with a "marks"
    key that is a list of the corresponding marks. If a name is not found, you can choose
    to return 0 or handle it as you wish.
    """
    # Retrieve marks in the order of the query parameters
    result = [marks_data.get(n, 0) for n in name]
    return {"marks": result}

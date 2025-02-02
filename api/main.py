from fastapi import FastAPI, Query
import json
from fastapi.responses import JSONResponse

app = FastAPI()

# Load the student data
with open("q-vercel-python.json", "r") as file:
    data = json.load(file)

@app.get("/")
async def read_marks(name: list[str] = Query([])):
    # Get marks for each name in the query
    marks = [data.get(n, "Not Found") for n in name]
    return JSONResponse(content={"marks": marks})

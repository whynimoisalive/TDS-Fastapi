from fastapi import FastAPI, Query
import json
from fastapi.responses import JSONResponse

app = FastAPI()

# Load the student data from q-vercel-python.json
with open("q-vercel-python.json", "r") as file:
    data = json.load(file)

@app.get("/")
async def get_marks(name: list[str] = Query([])):
    marks = [data.get(n, "Not Found") for n in name]
    return JSONResponse(content={"marks": marks})

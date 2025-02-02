import json
import os
from serverless_http import handler
from urllib.parse import parse_qs, urlparse

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')
    with open(file_path, 'r') as file:
        return json.load(file)

def app(environ, start_response):
    # Parse query parameters
    query = parse_qs(environ.get('QUERY_STRING', ''))
    names = query.get('name', [])
    
    # Load data
    data = load_data()
    
    # Prepare response
    result = {"marks": []}
    for name in names:
        for entry in data:
            if entry["name"] == name:
                result["marks"].append(entry["marks"])
    
    # Build headers
    headers = [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*')
    ]
    
    start_response('200 OK', headers)
    return [json.dumps(result).encode('utf-8')]

# Vercel handler
handle = handler(app)
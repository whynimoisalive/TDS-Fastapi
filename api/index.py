from flask import Flask, request, jsonify
import json
import os
from serverless_http import handle

app = Flask(__name__)

# Load marks data
with open(os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')) as f:
    marks_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [marks_data.get(name, 0) for name in names]
    response = jsonify({'marks': marks})
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

handler = handle(app)
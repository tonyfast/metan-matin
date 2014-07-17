"""REST API routes"""

from flask import jsonify
from metaregistry import app

@app.route('/')
def index():
    return jsonify(message='Derp.')

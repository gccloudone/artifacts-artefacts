from flask import Flask, jsonify, request
import json
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "python-flask-api",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

@app.route('/api/info')
def get_info():
    return jsonify({
        "service": "GC Secure Artifacts Python Demo",
        "description": "Minimal Flask API for Chainguard/JFrog POC",
        "features": [
            "Chainguard base image",
            "JFrog Artifactory integration",
            "Xray vulnerability scanning",
            "SBOM generation"
        ]
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        "received": data,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
    
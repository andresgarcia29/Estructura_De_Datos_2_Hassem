"""
    Flask Index
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS

APP = Flask('project')
CORS(APP)


@APP.route('/api/v1/healthz', methods=['GET'])
def healthz():
    """
        healthz endpoint to kubernetes
    """
    return jsonify(status=200), 200
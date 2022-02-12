from os import environ as env
from flask import Flask
from flask_cors import CORS


def init_server():
    
    server = Flask(__name__)
    CORS(server)
    server.config['CORS_HEADERS'] = 'Content-Type'
    server.run(host='0.0.0.0', port=int(env.get('PORT', 5000)), debug=True)
    
    return server

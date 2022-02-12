from flask import Flask
from flask_cors import CORS

def init_server():
    
    server = Flask(__name__)
    CORS(server)
    server.config['CORS_HEADERS'] = 'Content-Type'
    
    return server

from os import environ as env
from flask import Flask, request, render_template
from flask_cors import CORS

def main():
    
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    return app

if __name__ == '__main__':
    app = main()
    app.run(host='0.0.0.0', port=int(env.get('PORT', 5000)), debug=True)
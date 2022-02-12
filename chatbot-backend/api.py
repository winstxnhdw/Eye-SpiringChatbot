from os import environ as env
from flask import request
from server import init_server
from libs.debug import debug_print

app = init_server()

@app.route('/messages', methods=['POST'])
def reply():
    
    debug_print(f"Received message: {request.json['text']}")
    return request.json['text']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(env.get('PORT', 5000)), debug=True)
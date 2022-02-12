from flask import request
from server import init_server

app = init_server()

@app.route('/messages', methods=['POST'])
def reply():

    if request.method == 'POST':
        print(request.json['text'], flush=True)
        return request.json['text']
from os import environ as env
from flask import request
from server import init_server
from libs.debug import debug_print
from libs.chatbot import ChatBot

app = init_server()
bot = ChatBot()

@app.route('/messages', methods=['POST'])
def reply():
    
    debug_print(f"Received message: {request.json['text']}")
    return bot.reply(request.json['text'])

def main():
    app.run(host='0.0.0.0', port=int(env.get('PORT', 5000)), debug=True)

if __name__ == "__main__":
    main()
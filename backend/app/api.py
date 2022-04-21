from flask import request
from server import init_server
from config import Config
from libs.debug import debug_print
from libs.chatbot import ChatBot

app = init_server()
app.config.from_object(Config)
bot = ChatBot()

@app.route('/messages', methods=['POST'])
def reply() -> str:
    
    debug_print(f"Received message: {request.json['text']}")
    return bot.reply(request.json['text'])

def main():

    port = app.config['PORT']
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == "__main__":
    main()
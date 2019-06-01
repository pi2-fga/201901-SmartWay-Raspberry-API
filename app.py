from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
socketio = SocketIO(app)
# socketio.init_app(app, cors_allowed_origins=None)

@socketio.on('connect')
def connect():
    print('Client connected')

@socketio.on('alert')
def handle_message(message):
    print('recceived message: ' + message)
    send(message, broadcast=True)

@socketio.on('disconnect')
def disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    socketio.run(app, debug=True)
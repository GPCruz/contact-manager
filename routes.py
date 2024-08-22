from flask import Flask
from controller import handle_request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    return handle_request('register')

@app.route('/login', methods=['POST'])
def login():
    return handle_request('login')

# Adicione mais rotas conforme necessário
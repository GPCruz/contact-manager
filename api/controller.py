from flask import request, jsonify
from api.services.user_service import UserService

user_service = UserService()

def handle_request(endpoint):
    try:
        if endpoint == 'register':
            return register_user()
        elif endpoint == 'login':
            return login_user()
        # Adicione mais lógica de roteamento aqui
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    user = user_service.create_user(username, password)
    return jsonify({'message': 'User created successfully', 'user_id': user.id}), 201

def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    user = user_service.authenticate_user(username, password)
    if user:
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
    return jsonify({'error': 'Invalid username or password'}), 401
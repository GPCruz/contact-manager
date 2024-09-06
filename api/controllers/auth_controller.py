
from flask import jsonify, request

from api.services.auth_service import AuthService


def handle_login():
    username = request.headers.get('username')
    password = request.headers.get('password')
    token = AuthService.login(username = username, password = password)
    return jsonify({'token': token}), 200
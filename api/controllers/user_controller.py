from flask import jsonify, request

from services.user_service import UserService


def handle_create_user():
    username = request.headers.get('username')
    name = request.headers.get('name')
    password = request.headers.get('password')
    UserService.create_user(username = username, name = name, password = password)
    return 'User created', 201
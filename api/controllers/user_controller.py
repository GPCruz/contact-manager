from flask import request as req

from api.services.user_service import UserService


def handle_create_user():
    username = req.headers.get('username')
    password = req.headers.get('password')
    UserService.create_user(username = username, password = password)
    return 'User created', 201
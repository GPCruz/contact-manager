from flask import Blueprint

from api.controllers.user_controller import handle_create_user



main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    return "Hello World!"

@main_bp.route('/users', methods=['POST'])
def register():
    return handle_create_user()

@main_bp.route('/login', methods=['GET'])
    return handle_login()
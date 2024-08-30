from flask import Blueprint, request
from controllers.user_controller import create_user, get_all_users, get_user_by_id, update_user_by_id, delete_user_by_id

bp = Blueprint('user_bp', __name__)

@bp.route('/users', methods=['POST'])
def create_user_route():
    return create_user()

@bp.route('/users', methods=['GET'])
def get_users():
    return get_all_users()

@bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_by_id(user_id)

@bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    return update_user_by_id(user_id, user_data)

@bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_by_id(user_id)

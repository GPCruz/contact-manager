from flask import jsonify, request

from services.user_service import UserService


def create_user():
    data = request.get_json()
    user_service = UserService()
    
    try:
        user = user_service.create_user(data)
        return jsonify(user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def get_all_users():
    user_service = UserService()
    
    try:
        users = user_service.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def get_user_by_id(user_id):
    user_service = UserService()
    
    try:
        user = user_service.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def update_user_by_id(user_id, user_data):
    user_service = UserService()
    
    try:
        updated_user = user_service.update_user_by_id(user_id, user_data)
        if updated_user:
            return jsonify(updated_user), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def delete_user_by_id(user_id):
    user_service = UserService()
    
    try:
        success = user_service.delete_user_by_id(user_id)
        if success:
            return jsonify({"message": "User deleted"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
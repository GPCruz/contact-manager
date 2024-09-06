from db.db_driver import get_session
from db.models.user_model import User
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash


class UserService:
    @classmethod
    def create_user(cls, username, name, password):
        try:
            password_hash = generate_password_hash(password)
            new_user = User(username=username, name=name,
                            password_hash=password_hash)
            with get_session() as session:
                session.add(new_user)
            return new_user
        except SQLAlchemyError as e:
            print(f"Error creating user: {e}")
            return None

    @classmethod
    def authenticate_user(cls, username, password):
        try:
            with get_session() as session:
                user = session.query(User).filter_by(username=username).first()
                if user and check_password_hash(user.password_hash, password):
                    return user
            return None
        except SQLAlchemyError as e:
            print(f"Error authenticating user: {e}")
            return None

    @classmethod
    def get_user(self, user_id):
        try:
            with get_session() as session:
                return session.query(User).get(user_id)
        except SQLAlchemyError as e:
            print(f"Error retrieving user: {e}")
            return None

    @classmethod
    def update_user(self, user_id, username=None, password=None):
        try:
            with get_session() as session:
                user = session.query(User).get(user_id)
                if user:
                    if username:
                        user.username = username
                    if password:
                        user.password_hash = generate_password_hash(password)
                    return user
            return None
        except SQLAlchemyError as e:
            print(f"Error updating user: {e}")
            return None

    @classmethod
    def delete_user(self, user_id):
        try:
            with get_session() as session:
                user = session.query(User).get(user_id)
                if user:
                    session.delete(user)
                    return True
            return False
        except SQLAlchemyError as e:
            print(f"Error deleting user: {e}")
            return False

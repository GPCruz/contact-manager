from werkzeug.security import generate_password_hash, check_password_hash
from api.db.db_utils import transactional_session, read_only_session
from db.models.user_model import User
from db.db_driver import get_session
from sqlalchemy.exc import SQLAlchemyError


class UserService:
    @classmethod
    @transactional_session
    def create_user(cls, session, username, password):
        password_hash = generate_password_hash(password)
        new_user = User(username=username, password_hash=password_hash)
        session.add(new_user)
        return new_user
    
    @classmethod
    @read_only_session
    def authenticate_user(cls, session, username, password):
        user = session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None
    # def create_user(self, username, name, password):
    #     try:
    #         password_hash = generate_password_hash(password)
    #         new_user = User(username=username, name=name, password_hash=password_hash)
    #         with get_session() as session:
    #             session.add(new_user)
    #         return new_user
    #     except SQLAlchemyError as e:
    #         print(f"Error creating user: {e}")
    #         return None

    # def authenticate_user(self, username, password):
    #     try:
    #         with get_session() as session:
    #             user = session.query(User).filter_by(username=username).first()
    #             if user and check_password_hash(user.password_hash, password):
    #                 return user
    #         return None
    #     except SQLAlchemyError as e:
    #         print(f"Error authenticating user: {e}")
    #         return None

    def get_user(self, user_id):
        try:
            with get_session() as session:
                return session.query(User).get(user_id)
        except SQLAlchemyError as e:
            print(f"Error retrieving user: {e}")
            return None

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
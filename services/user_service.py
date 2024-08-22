from werkzeug.security import generate_password_hash, check_password_hash
from db.models.user_model import User
from db.db_driver import session

class UserService:
    def create_user(self, username, password):
        password_hash = generate_password_hash(password)
        new_user = User(username=username, password_hash=password_hash)
        session.add(new_user)
        session.commit()
        return new_user

    def authenticate_user(self, username, password):
        user = session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None
from werkzeug.security import generate_password_hash, check_password_hash
from api.db.db_utils import transactional_session, read_only_session
from api.db.models.user_model import User


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
from sqlalchemy import Column, Integer, String
from api.db.abstractions.base import Base
from datetime import datetime, timedelta
import jwt
from api.config import Config


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    def generate_auth_token(self):
        payload = {
            'user_id': self.id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
        return token
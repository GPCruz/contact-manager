from sqlalchemy import Column, Integer, String
from db.abstractions.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
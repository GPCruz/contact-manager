from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.config import Config
from api.db.abstractions.base import Base


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
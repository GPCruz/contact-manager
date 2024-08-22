from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from db.abstractions.base import Base


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Cria todas as tabelas
Base.metadata.create_all(engine)
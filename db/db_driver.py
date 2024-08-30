from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from config import Config
from db.abstractions.base import Base

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, poolclass=NullPool)
Session = sessionmaker(bind=engine)

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

# Cria todas as tabelas
Base.metadata.create_all(engine)
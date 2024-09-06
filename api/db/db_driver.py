from contextlib import contextmanager

from sqlalchemy import create_engine

from sqlalchemy.pool import NullPool

from sqlalchemy.orm import sessionmaker

from api.config import Config

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
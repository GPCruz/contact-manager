import logging
from functools import wraps

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from api.db.abstractions.base import Base

def get_engine():
    env = os.environ.get('ENV')
    suffix = '_DEV' if env == 'dev' else ''
    db_host = os.environ.get(f'DB_HOST{suffix}')
    db_port = os.environ.get(f'DB_PORT{suffix}')
    db_name = os.environ.get(f'DB_NAME{suffix}')
    db_user = os.environ.get(f'DB_USER{suffix}')
    db_password = os.environ.get(f'DB_PASSWORD{suffix}')
    return create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}', poolclass=NullPool)

def connect_engine():
    try:
        engine = get_engine()
        Session = sessionmaker(bind=engine)
        session = Session()
        logging.info('Connected to database')
        return session
    except Exception as e:
        raise ConnectionError(f'Failed to connect to database: {str(e)}')
    
def kill_engine(session):
    try:
        session.close()
        logging.info('Disconnected from database')
    except Exception as e:
        raise ConnectionError(f'Failed to disconnect from database: {str(e)}')
    
def get_column_names(entity_property):
    return entity_property.property.columns[0].key


def transactional_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = None
        try:
            session = connect_engine()
            result = func(session = session, *args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            if session:
                session.rollback()
            logging.error(f'Error in transaction: {str(e)}')
            raise e
        finally:
            if session:
                kill_engine(session)
    return wrapper

def read_only_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = connect_engine()
        try:
            result = func(session, *args, **kwargs)
            return result
        except Exception as e:
            logging.error(f'Error in read-only session: {str(e)}')
            raise e
        finally:
            kill_engine(session)
    return wrapper
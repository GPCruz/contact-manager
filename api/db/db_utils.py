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

def get_column_names(entity_property):
    return entity_property.property.columns[0].key

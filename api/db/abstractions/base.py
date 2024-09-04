from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Base(base):
    __abstract__ = True

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

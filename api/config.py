import os


class Config:

    DEBUG = os.environ.get('DEBUG', False)
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get(f'SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY')
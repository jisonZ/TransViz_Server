import os
import string
import random


letters = string.ascii_letters


class BaseConfig(object):
    """base config"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("secret_key", ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in range(16)]))


class TestingConfig(BaseConfig):
    """testing config"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """dev config"""
    DEBUG = True
    PORT = 6000
    SQLALCHEMY_DATABASE_URI = ''


class ProductionConfig(BaseConfig):
    """production config"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("")

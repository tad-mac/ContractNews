import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


# Enables Flask's debugging features. Should be False in Production
DEBUG = True

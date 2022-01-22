from os import getenv

SECRET_KEY = getenv('SECRET_KEY', None)
assert SECRET_KEY

FLASK_ENV = getenv('FLASK_ENV', 'development')
assert FLASK_ENV
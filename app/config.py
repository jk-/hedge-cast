import os


class base_config(object):
    SUPPORTED_LOCALES = ['en']

    SITE_NAME = os.environ.get(
        'APP_NAME',
        'Hedge Cast - Investment learning at your fingertips'
    )
    SECRET_KEY = os.environ.get('SECRET_KEY', 'itsasecret')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
    POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_PASS = os.environ.get('POSTGRES_PASS', 'mysecretpassword')
    POSTGRES_DB = os.environ.get('POSTGRES_DB', 'hedgecast')

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASS,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class test_config(base_config):
    TESTING = True
    WTF_CSRF_ENABLED = False

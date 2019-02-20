import os


class base_config(object):
    SUPPORTED_LOCALES = ['en']

    SITE_NAME = os.environ.get(
        'APP_NAME',
        'Hedge Cast - Investment learning at your fingertips'
    )
    SECRET_KEY = os.environ.get('SECRET_KEY', 'itsasecret')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    DATABASE_HOST = os.environ.get('DATABASE_HOST', '127.0.0.1')
    DATABASE_PORT = os.environ.get('DATABASE_PORT', 3306)
    DATABASE_USER = os.environ.get('DATABASE_USER', 'root')
    DATABASE_PASS = os.environ.get('DATABASE_PASS', 'pass')
    DATABASE_DB = os.environ.get('DATABASE_DB', 'hedgecast')

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%d/%s' % (
        DATABASE_USER,
        DATABASE_PASS,
        DATABASE_HOST,
        DATABASE_PORT,
        DATABASE_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class test_config(base_config):
    TESTING = True
    WTF_CSRF_ENABLED = False

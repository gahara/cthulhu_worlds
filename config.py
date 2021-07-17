import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    JSONIFY_PRETTYPRINT_REGULAR = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False


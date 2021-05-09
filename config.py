import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Vivalafrance@123@localhost:3306/parser?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

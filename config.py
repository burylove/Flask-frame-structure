#!/usr/bin/env python
#-*-coding:utf-8-*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
    r'\xa7\xdb\xfd\xcetp\xf2\x9df+\xe20\x92\x1f\x18\x90\xcb\x0b\xd8RY$3\x8b'
    
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    # 配置邮件信息
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass


# 定义开发环境类
class DevelopmentConfig(Config):
    DEBUG = True
    # 邮箱
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "zzz1171284619@gmail.com"
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or "zcf.19970125"

    #数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:12345679@localhost:3306/h1'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'mysql://root:12345679@localhost:3306/h1'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://root:12345679@localhost:3306/h1'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}





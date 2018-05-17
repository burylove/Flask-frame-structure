import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = r'\xa7\xdb\xfd\xcetp\xf2\x9df+\xe20\x92\x1f\x18\x90\xcb\x0b\xd8RY$3\x8b'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    # 配置邮件信息
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass





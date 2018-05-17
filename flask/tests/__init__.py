from flask import Flask, render_template    # 引入flask及模板
from flask_bootstrap import Bootstrap   # 引入bootstrap模板
from flask_mail import Mail     #引入邮件扩展
from flask_moment import Moment #引用时间戳扩
from flask_sqlalchemy import SQLAlchemy #引入数据库驱动
from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #初始化扩展
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #附加路由和定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app




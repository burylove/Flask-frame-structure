#!/usr/bin/env python
#-*-coding:utf-8-*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy #引用数据库，需要安装MySQL-python
import os
from flask_script import Manager

from flask import session, redirect,url_for # 引入重定向和用户会话
from flask import flash     #Flash消息

# 引入表单模块
from flask_wtf import Form
from wtforms import StringField, SubmitField    # 引入文本和提交按钮
from wtforms.validators import Required     # 引入校验
# from wtforms import PasswordField   # 引入密码输入框

from flask_moment import Moment # 本地化时间
from datetime import datetime   # 引入时间模块


app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# 自定义对象
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref = 'role',lazy = 'dynamic')
    #  backref 参数向 User 模型中添加一个 role 属性，从而定义反向关系

    def __repr__(self):
        return '<Role %r >' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True )
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 设置外键

    def __repr__(self):
        return '<User %r >' % self.username
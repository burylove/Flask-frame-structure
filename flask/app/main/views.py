#!/usr/bin/env python
#-*-coding:utf-8-*-
datetime import datetime   # 引入时间模块
from flask import render_template, session, redirect, url_for

# 引入本地模块
from . import main
from .forms import NameForm
from .. import db
from ..models import User


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


# 定义表单
class NameForm(Form):
    name = StringField('what is your name?', validators= [Required()])
    # required：必要的，必须的
    submit = SubmitField('submit')


@main.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        #...
        return redirect(url_for('.index'))
    return render_template('index.html', form = form, 
                            name = session.get('name'),
                            known = session.get('known',False),
                            current_time = datetime.utcnow())











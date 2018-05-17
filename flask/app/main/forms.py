#!/usr/bin/env python
#-*-coding:utf-8-*-
# 引入表单模块
from flask_wtf import Form
from wtforms import StringField, SubmitField    # 引入文本和提交按钮
from wtforms.validators import Required     # 引入校验
# from wtforms import PasswordField   # 引入密码输入框

# 定义表单
class NameForm(Form):
    name = StringField('what is your name?', validators= [Required()])
    # required：必要的，必须的
    submit = SubmitField('submit')
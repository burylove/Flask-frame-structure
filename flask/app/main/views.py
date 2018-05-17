#!/usr/bin/env python
#-*-coding:utf-8-*-
datetime import datetime   # 引入时间模块
from flask import render_template, session, redirect, url_for

# 引入本地模块
from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        #...
        return redirect(url_for('.index'))
    return render_template('lw-index.html', form = form, 
                            name = session.get('name'),
                            known = session.get('known',False),
                            current_time = datetime.utcnow())











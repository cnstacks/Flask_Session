#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 16:53
# File    : account.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Blueprint, render_template, request, session, redirect
from uuid import uuid4
from ..utils.sql import SQLHelper

account = Blueprint('account', __name__)


@account.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    user = request.form.get('user')
    pwd = request.form.get('pwd')

    # 连接数据库查询;
    obj = SQLHelper.fetch_one("select id,name from users where name=%s and pwd = %s", [user, pwd, ])

    # print(obj)
    if obj:
        uid = str(uuid4())
        session.permanent = True
        session['user_info'] = {'id': obj['id'], 'name': user}
        return redirect('/index/')
    else:
        return render_template('login.html', msg='用户名或者密码错误！')

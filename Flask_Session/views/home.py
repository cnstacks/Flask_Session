#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 17:33
# File    : home.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from flask import Blueprint, render_template, request, session, redirect

home = Blueprint('home', __name__)


@home.route('/index/', methods=['GET', 'POST'])
def index():
    user_info = session.get('user_info')  # {'k1':1,'k2':2}
    print("原来的值", user_info)
    session['user_info']['k1'] = 19939
    user_info = session.get('user_info')
    print("修改之后的值", user_info)
    # session['modified'] = True,在配置文件中使用SESSION_REFRESH_EACH_REQUEST代替;
    return 'Index'


@home.route('/test/')
def test():
    user_info = session.get('user_info')
    print(user_info)
    return 'Test'

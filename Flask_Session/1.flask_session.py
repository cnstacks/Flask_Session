#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 16:14
# File    : 1.flask_session.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask, session
from flask_session import RedisSessionInterface

app = Flask(__name__)
app.secret_key = 'fdahfdafdajfalk'

# 默认session保存操作；
# from flask.sessions import SecureCookieSessionInterface

# app.session_interface = SecureCookieSessionInterface()

# 使用Redis保存session;
from flask.ext.session import Session
from redis import Redis

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='192.168.0.94', port='6379')
app.session_interface = RedisSessionInterface(
    redis=Redis(host='127.0.0.1', port=6379),
    key_prefix='flaskxxxx'

)


@app.route('/login/')
def login():
    session['k1'] = 123
    return 'Login'


@app.route('/index/')
def index():
    v = session['k1']
    print(v)
    return 'Index'


if __name__ == '__main__':
    app.run()

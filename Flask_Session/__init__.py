#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 16:46
# File    : __init__.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask
from .views import account
from .views import home


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')
    app.register_blueprint(account.account)
    app.register_blueprint(home.home)
    return app

#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 16:46
# File    : manage.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from Flask_Session import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

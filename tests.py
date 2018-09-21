#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 18:43
# File    : tests.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from redis import Redis

conn = Redis(host='127.0.0.1')
v = conn.keys()
print(v)
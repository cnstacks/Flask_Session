#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 19:53
# File    : MySQL数据库练习.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


import pymysql

conn = pymysql.connect(host='x.x.x.x', port=3306, user='root', passwd='Tqtl911!@%*)', db='flask_session')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select id,name from users where name = %s and pwd = %s", ['cxz', '123', ])
obj = cursor.fetchone()
conn.commit()
cursor.close()

conn.close()

print(obj)

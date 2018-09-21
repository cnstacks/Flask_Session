#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 20:13
# File    : sql.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
import pymysql


class SQLHelper(object):
    @staticmethod
    def open():
        conn = pymysql.connect(host='x.x.x.x', port=3306, user='root', passwd='Tqtl911!@%*)',
                               db='flask_session')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    @staticmethod
    def close(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def fetch_one(cls, sql, args):
        # cursor.execute("select id,name from users where name = %s and pwd = %s", ['cxz', '123', ])
        conn, cursor = cls.open()
        cursor.execute(sql, args)
        obj = cursor.fetchone()
        cls.close(conn, cursor)
        return obj

    @classmethod
    def fetch_all(cls, sql, args):
        conn, cursor = cls.open()
        cursor.execute(sql, args)
        obj = cursor.fetchall()
        cls.close(conn, cursor)
        return obj

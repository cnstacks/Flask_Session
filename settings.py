#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: Flask_Session 
# Software: PyCharm
# Time    : 2018-09-20 17:28
# File    : settings.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from datetime import timedelta
from redis import Redis


class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite://:memory'
    SECRET_KEY = 'fjdksjfdasljflksd'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)
    SESSION_REFRESH_EACH_REQUEST = True
    SESSION_TYPE = "redis"
    #SESSION_REDIS = Redis(host='127.0.0.1',port='6379')


class ProductionConfig(Config):
    SESSION_REDIS = Redis(host='127.0.0.1', port='6379')


class DevelopmentConfig(Config):
    SESSION_REDIS = Redis(host='127.0.0.1', port='6379')


class TestingConfig(Config):
    SESSION_REDIS = Redis(host='127.0.0.1', port='6379')

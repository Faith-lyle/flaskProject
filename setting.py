#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: flaskProject>>setting.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/5/18-08:21
@IDE: PyCharm 
"""

FLASK_DEBUG = True

# 数据库配置
IP = '10.102.133.31'
PORT = 3306
USER_NAME = 'root'
PASS_WORD = 'admin1234'
DATA_BASE = 'web_data'
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER_NAME}:{PASS_WORD}@{IP}:{PORT}/{DATA_BASE}?charset=utf8"
SQLALCHEMY_COMMIT_ON_TEARDOWN  = True

# Form表单启动CSRF保护，可以在config.py中定义2个变量：
CSRF_ENABLED = True
SECRET_KEY = '123456'

#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: flaskProject>>extend.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/5/18-08:21
@IDE: PyCharm 
"""
from os import path

from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

basedir = path.abspath(path.dirname(__file__))
login_manager = LoginManager()

# Form表单
class Login(FlaskForm):
    account = StringField(u'账号', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'登录')

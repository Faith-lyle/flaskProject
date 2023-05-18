#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: flaskProject>>module.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/5/18-08:34
@IDE: PyCharm 
"""
import datetime

from flask_login import UserMixin

from extend import db


class Account(UserMixin,db.Model):
    __tablename__ = 'Account'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64))
    pass_word = db.Column(db.String(64))
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def get_id(self):
        return self.id

    def verify_password(self, password):
        if password == self.pass_word:
            return True
        else:
            return False

    def __repr__(self):
        return '<Admin %r>' % self.user_name

#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: flaskProject>>mainView.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/5/18-08:40
@IDE: PyCharm 
"""
from flask import Blueprint, url_for, redirect, session,render_template
from extend import login_manager
from module import Account

bp = Blueprint('/', __name__)


@login_manager.user_loader
def load_user(admin_id):
    return Account.query.get(int(admin_id))


@bp.route('/')
def index():
    print()
    if Account.query.get(int(session['admin_id'])):
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))

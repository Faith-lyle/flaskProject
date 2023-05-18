#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: flaskProject>>auth.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/5/18-08:40
@IDE: PyCharm 
"""
from flask import Blueprint, render_template, flash, session, redirect, url_for
from extend import basedir, Login
from module import Account
from flask_login import login_user

bp = Blueprint('auth', __name__, template_folder=f'{basedir}/template', static_folder=f'{basedir}/static')


@bp.route('/login', methods=['GET', "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        user = Account.query.filter_by(id=form.account.data, pass_word=form.password.data).first()
        if user is None:
            flash('账号或密码错误！')
            return redirect(url_for('auth.login'))
        else:
            login_user(user)
            session['admin_id'] = user.id
            session['name'] = user.user_name
            return 'successful'
    return render_template('login.html', form=form)

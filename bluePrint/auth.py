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
from extend import basedir, Login, EditInfoForm, db, ChangePasswordForm
from module import Account
from flask_login import login_user, logout_user, login_required, current_user, LoginManager

bp = Blueprint('auth', __name__, template_folder=f'{basedir}/template', static_folder=f'{basedir}/static')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(admin_id):
    return Account.query.get(int(admin_id))


@bp.route('/login', methods=['GET', "POST"])
# @login_required
def login():
    form = Login()
    if form.validate_on_submit():
        user = db.session.query(Account).filter_by(id=form.account.data, pass_word=form.password.data).first()
        if user is None:
            flash('账号或密码错误！')
            return redirect(url_for('auth.login'))
        else:
            login_user(user)
            session['admin_id'] = user.id
            session['name'] = user.user_name
            return redirect(url_for('/.index'))
    return render_template('login.html', form=form)


@bp.route('/logout')
# @login_required
def logout():
    logout_user()
    flash('您已经登出！')
    return redirect(url_for('auth.login'))


@bp.route('/info')
def info():
    return render_template('user-info.html', admin_id=session['admin_id'], admin_name=session['name'])


@bp.route('/change_password', methods=['GET', 'POST'])
# @login_required
def change_password():
    form = ChangePasswordForm()
    if form.password2.data != form.password.data:
        flash(u'两次密码不一致！')
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            # r1 = db.session.flush(current_user)

            db.session.query(Account).filter_by(id=current_user.id).update({"pass_word":current_user.password})
            r = db.session.commit()
            flash(u'修改密码成功！')
            return redirect(url_for('/.index'))
        else:
            flash(u'原密码输入错误，修改失败！')
    return render_template("change-password.html", form=form)

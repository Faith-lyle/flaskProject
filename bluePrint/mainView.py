#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: flaskProject>>mainView.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/5/18-08:40
@IDE: PyCharm 
"""
from flask import Blueprint, url_for, redirect, session, render_template
from module import Account

bp = Blueprint('/', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    if 'admin_id' in session.keys():
        if Account.query.get(int(session['admin_id'])):
            # print(session['user_name'])
            return render_template('index.html', name=session['name'])
        else:
            return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))


@bp.route('/h29_main')
def h29_main():
    return render_template('h29_main.html', name=session['name'])


@bp.route('/get_data1')
def get_data1():
    fail_datas = [
        ['1', '制程', 'DZ0211空焊', '11', '28.95%', 28.95, 'On going', 'PE', '2/21'],
        ['2', '制程', 'DZ0201空焊', '5', '13.16%', 42.11, 'On going', 'PE', '2/21 '],
        ['3', '制程', 'DZ0215空焊', '4', '13.16%', 42.11, 'On going', 'PE', '2/21 '],
        ['4', '制程', 'DZ0214空焊', '4', '13.16%', 63.16, 'close', 'PE', '2/21 '],
        ['5', '制程', 'DZ0210空焊', '4', '13.16%', 73.68, 'close', 'PE', '2/21 '],
        ['6', '制程', 'DZ0202空焊', '4', '13.16%', 84.21, 'close', 'PE', '2/21 '],
        ['7', '制程', 'DZ0213空焊', '3', '13.16%', 92.11, 'close', 'PE', '2/21 '],
        ['8', '制程', 'J0201空焊', '3', '13.16%', 100, 'close', 'PE', '2/21 '],
    ]
    script = '''
<script >
    $('td:contains("On going")').css("color","yellow")
    $('td:contains("close")').css("color","lime")
</script>
    '''
    data = {
        'fail_datas': fail_datas,
        "html": render_template('demo.html', fail_datas=fail_datas),
        'script':script
    }
    return data


@bp.route('/get_data')
def get_data():
    fail_datas = [
        ['1', '制程', 'DZ0211空焊', '11', '28.95%', '28.95', 'On going', 'PE', '2/21'],
        ['2', '制程', 'DZ0201空焊', '5', '13.16%', '42.11', 'On going', 'PE', '2/21 '],
        ['3', '制程', 'DZ0215空焊', '4', '13.16%', '42.11', 'On going', 'PE', '2/21 '],
        ['4', '制程', 'DZ0214空焊', '4', '13.16%', '63.16', 'close', 'PE', '2/21 '],
        ['5', '制程', 'DZ0210空焊', '4', '13.16%', '73.68', 'close', 'PE', '2/21 '],
        ['6', '制程', 'DZ0202空焊', '4', '13.16%', '84.21', 'close', 'PE', '2/21 '],
        ['7', '制程', 'DZ0213空焊', '3', '13.16%', '92.11', 'close', 'PE', '2/21 '],
        ['8', '制程', 'J0201空焊', '3', '13.16%', "100", 'close', 'PE', '2/21 '],
    ]

    return render_template('demo.html', fail_datas=fail_datas)

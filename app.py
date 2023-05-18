from flask import Flask
from flask_login import LoginManager

from extend import db, basedir, login_manager
from bluePrint.auth import bp as abp
from bluePrint.mainView import bp as mbp
from flask_script import Manager, Shell
from module import Account

app = Flask(__name__)
manager = Manager(app)
app.register_blueprint(abp, url_prefix='/auth', static_fold=f'{basedir}/static', template_folder=f'{basedir}/template')
app.register_blueprint(mbp)

app.config.from_pyfile('setting.py')

db.init_app(app)
login_manager.init_app(app)


def make_shell_context():
    return dict(app=app, db=db, Account=Account)


login_manager.session_protection = 'basic'
login_manager.login_view = 'login'
login_manager.login_message = u"请先登录。"
manager.add_command("shell", Shell(make_context=make_shell_context))




if __name__ == '__main__':
    app.debug = True
    manager.run()

import logging
#从flask包中导入Flask类
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from config import Config
from logging.handlers import RotatingFileHandler
import os
from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate
from flask_login import LoginManager


# 将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)  # 迁移引擎对象

login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app)
bootstrap = Bootstrap(app)

# 从app包中导入模块routes
from app import routes, models, errors


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-17 15:17

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import configs

app = Flask(__name__)
app.config.from_object(configs['dev'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'

from app import route, models
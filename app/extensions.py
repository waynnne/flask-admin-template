# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-12-04 01:19

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
# cors = CORS()
bootstrap = Bootstrap()
login = LoginManager()
login.login_view = 'auth.login'
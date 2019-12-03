# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-17 15:17

from flask import Flask

from config import configs
from app.admin.public import public_bp
from app.admin.auth import auth_bp
from app.extensions import db, migrate, bootstrap,login


def create_app(config_name=None):
    ''' 工厂模式创建app '''
    app = Flask(__name__)
    configure_app(app, config_name)
    configure_extensions(app)
    configure_blueprints(app)
    return app


def configure_app(app, config_name):
    ''' 初始化配置 '''
    if not config_name:
        config_name = 'dev'
    app.config.from_object(configs[config_name])
    # 不检查url尾部是否有斜杠 /
    app.url_map.strict_slashes = False


def configure_extensions(app):
    ''' 配置扩展 '''
    db.init_app(app)
    migrate.init_app(app, db)
    # cors.init_app(app)
    bootstrap.init_app(app)
    login.init_app(app)


def configure_blueprints(app):
    ''' 注册蓝图 '''
    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

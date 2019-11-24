# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-18 23:25

class Config(object):
    ''' 基础配置 '''
    DEBUG = True
    # Mysql配置
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    ''' 开发环境配置 '''
    SECRET_KEY = "dev_secret_key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:Qwerty123!@#@127.0.0.1:3306/flask_admin?charset=utf8"

class ProdConfig(Config):
    ''' 生产环境配置 '''
    DEBUG = False
    SECRET_KEY = "prod_secret_key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:youwillneverguess@127.0.0.1:3306/flask_admin?charset=utf8"


configs = {
    'dev': DevConfig,
    'prod': ProdConfig
}
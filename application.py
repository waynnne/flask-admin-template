# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-17 16:07

from app import create_app
# from app.models.auth_model import User

app = create_app('dev')

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User}
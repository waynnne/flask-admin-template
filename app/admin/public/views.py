# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-12-03 23:34

from flask import render_template
from flask_login import login_required
from app.admin.public import public_bp
from app.extensions import db


@public_bp.route('/')
@public_bp.route('/index')
def index():
    return "Hello, Flask!"


@public_bp.route('/modal')
@login_required
def modal():
    return render_template("public/modal.html")


@public_bp.route('/admin')
@login_required
def admin():
    # TODO 用户信息传递
    user = {
        'username': '管理员',
        'email': 'waynnne@mail.com'
    }
    return render_template("public/index.html", user=user)


@public_bp.app_errorhandler(404)
def not_fund_error(error):
    return render_template('public/404.html'), 404


@public_bp.app_errorhandler(500)
def internal_server_error(error):
    db.session.roll_back()
    return render_template('public/500.html'), 500

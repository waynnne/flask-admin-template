# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-12-03 23:34

from flask import render_template
from flask_login import login_required
from app.admin.public import public_bp



@public_bp.route('/')
@public_bp.route('/index')
def index():
    return "Hello, Flask!"


@public_bp.route('/admin')
@login_required
def admin():
    # TODO 用户信息传递
    user = {
        'username': 'waynnne',
        'email': 'waynnne@mail.com'
    }
    return render_template("public/index.html", user=user)
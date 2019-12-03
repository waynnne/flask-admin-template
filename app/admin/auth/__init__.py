# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-12-03 23:24

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from app.admin.auth import views
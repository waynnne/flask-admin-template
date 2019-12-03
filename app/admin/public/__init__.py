# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-12-03 23:28

from flask import Blueprint

public_bp = Blueprint('public', __name__)

from app.admin.public import views
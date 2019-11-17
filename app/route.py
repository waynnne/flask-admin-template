# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-17 16:10

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask!"
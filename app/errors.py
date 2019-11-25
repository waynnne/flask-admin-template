# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-25 23:36

from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_fund_error(error):
    return render_template('public/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    render_template('public/500.html'), 500
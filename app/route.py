# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-17 16:10

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask!"

@app.route('/home')
def home():
    return render_template("public/home.html")

@app.route('/about')
def about():
    return render_template("public/about.html")
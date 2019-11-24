# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-17 16:10

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegisterForm


@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask!"

@app.route('/home')
def home():
    return render_template("home/public/home.html")

@app.route('/about')
def about():
    return render_template("home/public/about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('用户 {} 登录'.format(form.username.data))
        return redirect(url_for('home'))
    render_template('home/auth/login.html', form=form)

@app.route('/admin')
def admin():
    return render_template("admin/index.html")

@app.route('/login1', methods=['GET', 'POST'])
def login1():
    form = LoginForm()
    if form.validate_on_submit():
        flash('用户 {} 登录成功！'.format(form.username.data))
        return redirect(url_for('admin'))
    return render_template("admin/templates/auth/login.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('用户 {} 注册成功！'.format(form.username.data))
        return redirect(url_for('login1'))
    return render_template("admin/templates/auth/register.html", form=form)
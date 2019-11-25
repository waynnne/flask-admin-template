# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-17 16:10

from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User
from app.forms import LoginForm, RegisterForm


@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask!"


@app.route('/admin')
@login_required
def admin():
    # TODO 用户信息传递
    user = {
        'username': 'waynnne',
        'email': 'waynnne@mail.com'
    }
    return render_template("admin/index.html", user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('用户名或密码错误！')
            return redirect(url_for('login'))
        login_user(user)
        flash('用户 {} 登录成功！'.format(form.username.data))
        return redirect(url_for('admin'))
    return render_template("auth/login.html", form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('用户 {} 注册成功！'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template("auth/register.html", form=form)
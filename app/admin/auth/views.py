# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-17 16:10

from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.extensions import db
from app.models.auth_model import User
from app.admin.auth.forms import LoginForm, RegisterForm
from app.admin.auth import auth_bp


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('用户名或密码错误！') # TODO 提示信息优化
            return redirect(url_for('auth.login'))
        login_user(user)
        flash('用户 {} 登录成功！'.format(form.username.data))
        return redirect(url_for('public.admin'))
    return render_template("auth/login.html", form=form)


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('public.admin'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('用户 {} 注册成功！'.format(form.username.data)) # TODO 提示信息优化
        return redirect(url_for('auth.login'))
    return render_template("auth/register.html", form=form)
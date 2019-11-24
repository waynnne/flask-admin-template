# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-18 23:51

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('登录')
    fa_addon = {
        'username': 'fa-user',
        'password': 'fa-lock',
    }


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('注册')
    fa_addon = {
        'username': 'fa-user',
        'email': 'fa-envelope',
        'password': 'fa-lock',
    }
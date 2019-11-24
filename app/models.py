# -*- coding: utf-8 -*-
# Author : waynnne
# Date   : 2019-11-19 23:57

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    pasword_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
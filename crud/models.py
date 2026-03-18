from connect_db import db


# user model
"""
name,
email,
password,
username,
is_verified
"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    is_verified = db.Column(db.Boolean, default=False)


# create todo model
"""
title,
description,
is_completed,
user_id (foreign key to User)
priority (low, medium, high)
"""


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(20), nullable=False, default="medium")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("todos", lazy=True))

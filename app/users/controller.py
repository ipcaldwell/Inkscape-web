# -*- coding: utf-8 -*-

from datetime import datetime
from hashlib import sha256
from os import urandom

import scrypt
from flask import Flask
from flask.ext.mail import Message
from flask.ext.sqlalchemy import SQLAlchemy

from app import app, db, login_manager, mail
from .model import Token, User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def create_user(username, email, password, accept_tos):
    salt = generate_salt()
    user = User(
            username,
            encrypt_password(password, salt),
            salt,
            email,
            accept_tos
            )
    db.session.add(user)
    db.session.commit()
    return user

def is_password_correct(user, password_given):
    result = False
    try:
        if scrypt.decrypt(user.password, '{0}:{1}:{2}'.format(app.config['SITE_SALT'], password_given, user.salt), maxtime=0.5) == app.config['SECRET_MESSAGE']:
            result = True
    except scrypt.error:
        app.logger.warning("Password was incorrect for user '{0}' (failed attempts: {1})".format(user.username, user.failed_logins))
    return result

def generate_salt(length=32):
    return urandom(length)

def generate_token(length=64):
    return sha256(urandom(64)).hexdigest()

def encrypt_password(password, salt):
    return scrypt.encrypt(app.config['SECRET_MESSAGE'], '{0}:{1}:{2}'.format(app.config['SITE_SALT'], password, salt), maxtime=0.5)

def decrypt_password(password, salt):
    return scrypt.decrypt('{0}:{1}:{2}'.format(app.config['SITE_SALT'], password, salt), maxtime=0.5)

def mail_user(user, subject, body=None, html=None, attachment=None):
    msg = Message(subject=subject, recipients=[user.email], body=body, html=html)
    if attachment is not None:
        msg.attach(attachment.filename, attachment.content_type, attachment.data, attachment.disposition)
    mail.send(msg)

def prevalidate_user(user):
    token = Token(user.id, generate_token())
    db.session.add(token)
    db.session.commit()
    mail_user(
            user,
            _("[Inkscape.org] Complete Your Registration"),
            _("""Please complete your registration by clicking the link below.

            http://inkscape.org/user/validate/{}/{}

            Thank you,
            The Inkscape Web Team""").format(user.email, token),
            )

def validate_user(user, given_token):
    print(user.token[0].name)
    print(given_token)
    if user.token[0].name == given_token:
        user.is_validated = True
        user.date_validated = datetime.now()
        db.session.commit()
        return True
    return False

def register_user(username, email, password, accept_tos):
    user = create_user(username, email, password, accept_tos)
    prevalidate_user(user)
    return user

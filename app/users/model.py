# -*- coding: utf-8 -*-

from sqlalchemy.sql import func
from sqlalchemy import event
from sqlalchemy.dialects.mysql import VARBINARY

from app import db

class Token(db.Model):
    __tablename__ = 'user_tokens'
    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.Unicode(64), nullable=False, unique=True)
    date_created = db.Column(db.TIMESTAMP(timezone=True), nullable=False, server_default=func.current_timestamp())

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.name = token

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    username = db.Column(db.Unicode(50), nullable=False, unique=True)
    password = db.Column(VARBINARY(200), nullable=False)
    salt = db.Column(VARBINARY(32), nullable=False)
    email = db.Column(db.Unicode(255), nullable=False)
    is_tos_accepted = db.Column(db.Boolean, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, server_default='0')
    is_banned = db.Column(db.Boolean, nullable=False, server_default='0')
    is_validated = db.Column(db.Boolean, nullable=False, server_default='0')
    is_email_public = db.Column(db.Boolean, nullable=False, server_default='0')
    is_superuser = db.Column(db.Boolean, nullable=False, server_default='0')
    date_created = db.Column(db.TIMESTAMP(timezone=True), nullable=False, server_default=func.current_timestamp())
    date_validated = db.Column(db.TIMESTAMP(timezone=True))
    date_last_login = db.Column(db.TIMESTAMP(timezone=True))
    date_deleted = db.Column(db.TIMESTAMP(timezone=True), nullable=True)
    logins = db.Column(db.Integer, nullable=False, server_default='0')
    failed_logins = db.Column(db.Integer, nullable=False, server_default='0')
    password_resets = db.Column(db.Integer, nullable=False, server_default='0')
    first_ip = db.Column(db.String(50))
    last_ip = db.Column(db.String(50))
    must_change_password = db.Column(db.Boolean, nullable=False, server_default='0')
    oauth_token = db.Column(db.String(200))
    oauth_secret = db.Column(db.String(200))
    token = db.relationship('Token', backref=db.backref('users', uselist=False))
    locale = db.Column(db.String(2), nullable=False, server_default="en")
    timezone = db.Column(db.String(50), nullable=False, server_default="America/Chicago")
    dateformat = db.Column(db.String(50), nullable=False, server_default="medium")

    def __init__(self, username, password, salt, email, is_tos_accepted):
        self.username = username
        self.password = password
        self.salt = salt
        self.email = email
        self.is_tos_accepted = is_tos_accepted

    def __repr__(self):
        return "<User #{}: {}>".format(self.id, self.username)

    # below 4 methods are for Flask-Login
    def is_authenticated(self):
        return True

    def is_active(self):
        return not self.is_deleted and self.is_validated

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    name = db.Column(db.Unicode(50), nullable=False, unique=True)
    is_active = db.Column(db.Boolean, nullable=False, server_default='1')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Role #{}: {}>".format(self.id, self.name)

def after_create(target, connection, **kw):
    [connection.execute(target.insert(), {'name': role}) for role in ['user', 'author', 'admin']]
event.listen(Role.__table__, 'after_create', after_create)

users_roles = db.Table('users_roles',
        db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
        )

class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    name = db.Column(db.Unicode(50), nullable=False, unique=True)
    is_active = db.Column(db.Boolean, nullable=False, server_default='1')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Permission #{}: {}>".format(self.id, self.name)

roles_permissions = db.Table('roles_permissions',
        db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
        db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id')),
        )

#db.session.add_all([
#        Permission('role-add'),
#        Permission('role-edit'),
#        Permission('role-delete'),
#        Permission('role-validate'),
#        Permission('role-ban'),
#        Permission('comment-add'),
#        Permission('comment-edit'),
#        Permission('comment-delete'),
#        Permission('comment-validate'),
#        Permission('news-add'),
#        Permission('news-edit'),
#        Permission('news-delete'),
#        Permission('news-validate'),
#        Permission('faq-add'),
#        Permission('faq-edit'),
#        Permission('faq-delete'),
#        Permission('faq-validate'),
#        Permission('art-add'),
#        Permission('art-edit'),
#        Permission('art-delete'),
#        Permission('art-validate'),
#        Permission('extension-add'),
#        Permission('extension-edit'),
#        Permission('extension-delete'),
#        Permission('extension-validate'),
#        Permission(''),
#        ])
#db.session.commit()

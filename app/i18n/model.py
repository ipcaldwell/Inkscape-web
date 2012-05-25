# -*- coding: utf-8 -*-

from sqlalchemy.sql import func
from sqlalchemy import event

from app import db

class Language(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True)
    code = db.Column(db.Unicode(3), nullable=False, unique=True)
    name = db.Column(db.Unicode(200), nullable=False)
    native_name = db.Column(db.Unicode(200), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, server_default='1')
    is_major = db.Column(db.Boolean, nullable=False, server_default='0')

    def init(self, code, name, native_name):
        self.code = code
        self.name = name
        self.native_name = native_name

    def __repr__(self):
        return '<Language #{}: {} ({}; {})'.format(self.id, self.code, self.name, self.native_name)

    """
    'en','English','English'
    'de','German','Deutsch'
    'fr','French','Français'
    'it','Italian','Italiano'
    'es','Spanish','Español'
    'pt','Portuguese','Português'
    'cs','Czech','Česky'
    'ru','Russian','Русский'
    'ja','Japanese','日本語'
    """

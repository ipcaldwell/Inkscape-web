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
    sort = db.Column(db.Integer, nullable=False, server_default='99999')

    def init(self, code, name, native_name):
        self.code = code
        self.name = name
        self.native_name = native_name

    def __repr__(self):
        return u'<Language #{}: {} ({}; {})'.format(self.id, self.code, self.name, self.native_name)

    """
    insert into `languages` (code, name, native_name, is_major, sort) values
    ('en','English','English', 1, 1),
    ('de','German','Deutsch', 1, 2),
    ('fr','French','Français', 1, 3),
    ('it','Italian','Italiano', 1, 4),
    ('es','Spanish','Español', 1, 5),
    ('pt','Portuguese','Português', 1, 6),
    ('cs','Czech','Česky', 1, 7),
    ('ru','Russian','Русский', 1, 8),
    ('ja','Japanese','日本語', 1, 9);

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

# -*- coding: utf-8 -*-

from sqlalchemy.sql import func
from sqlalchemy import event

from app import app, db

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

def after_create(target, connection, **kw):
    for index, language in enumerate(app.config['LANGUAGES']):
        connection.execute(target.insert(), {'code': language['code'], 'native_name': language['native_name'], 'name': language['name'], 'sort': index, 'is_major': 1})
event.listen(Language.__table__, 'after_create', after_create)

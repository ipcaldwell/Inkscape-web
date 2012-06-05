# -*- coding: utf-8 -*-

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = True

# Administrative
ADMINS = frozenset(['webmaster@inkscape.org'])

# Internationalization
LANGUAGES = (
    {u'code': u'en', u'name': u'English'},
    {u'code': u'de', u'name': u'Deutsch'},
    {u'code': u'fr', u'name': u'Français'},
    {u'code': u'it', u'name': u'Italiano'},
    {u'code': u'es', u'name': u'Español'},
    {u'code': u'pt', u'name': u'Português'},
    {u'code': u'cs', u'name': u'Česky'},
    {u'code': u'ru', u'name': u'Русский'},
    {u'code': u'ja', u'name': u'日本語'},
    )

# Database
DB_TYPE = '<ENGINE>'
DB_HOST = '<HOST>'
DB_USERNAME = '<USER>'
DB_PASSWORD = '<PASSWORD>'
DB_DATABASE = '<DATABASE>'

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}/{4}'.format(DB_TYPE, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_DATABASE)
SQLALCHEMY_ECHO = True
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

# Security
SECRET_KEY = b'<SECRET_KEY>'
SITE_SALT = b'<SITE_SALT>'
SECRET_MESSAGE = "<MESSAGE>"

CSRF_ENABLED = True
CSRF_SESSION_KEY = '<SESSION_KEY>'

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '<PUBLIC_KEY>'
RECAPTCHA_PRIVATE_KEY = '<PRIVATE_KEY>'
RECAPTCHA_OPTIONS = {'theme': 'white'}

# Mail
MAIL_SERVER = '<HOST>'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = DEBUG
MAIL_USERNAME = None
MAIL_PASSWORD = None
DEFAULT_MAIL_SENDER = ("Inkscape.org", 'webmaster@inkscape.org')

# AJAX
SIJAX_STATIC_PATH = os.path.join(_basedir, 'static/js/sijax/')
SIJAX_JSON_URI = '/static/js/sijax/json2.js'

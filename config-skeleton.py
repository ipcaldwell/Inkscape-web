# -*- coding: utf-8 -*-

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TESTING = True

# Administrative
ADMINS = frozenset(['webmaster@inkscape.org'])

# Internationalization
LANGUAGES = (
    {u'code': u'en', u'name': u'English', u'native_name': u'English'},
    {u'code': u'de', u'name': u'German', u'native_name': u'Deutsch'},
    {u'code': u'fr', u'name': u'French', u'native_name': u'Français'},
    {u'code': u'it', u'name': u'Italian', u'native_name': u'Italiano'},
    {u'code': u'es', u'name': u'Spanish', u'native_name': u'Español'},
    {u'code': u'pt', u'name': u'Portuguese', u'native_name': u'Português'},
    {u'code': u'cs', u'name': u'Czech', u'native_name': u'Česky'},
    {u'code': u'ru', u'name': u'Russian', u'native_name': u'Русский'},
    {u'code': u'ja', u'name': u'Japanese', u'native_name': u'日本語'},
    )
SUPPORTED_LOCALES = [language['code'] for language in LANGUAGES]

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

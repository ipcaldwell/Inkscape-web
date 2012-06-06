# -*- encoding: utf-8 -*-

from flask import Blueprint, flash, g, Markup, redirect, render_template, request, session, url_for
from werkzeug.routing import Rule, Submount

from app import app, babel
from ..decorators import crumbs
from . import db, module, Language
import controller
from ..news import view as news_view

@app.url_defaults
def add_language_code(endpoint, values):
    if endpoint == 'static':
        return
    values.setdefault('language_code', g.language_code)

@app.url_value_preprocessor
def pull_language_code(endpoint, values):
    if endpoint == 'static':
        return
    if values is not None:
        g.language_code = values.pop('language_code', request.accept_languages.best_match(app.config['SUPPORTED_LOCALES']))
    else:
        g.language_code = request.accept_languages.best_match(app.config['SUPPORTED_LOCALES'])

@babel.localeselector
def get_locale():
    app.logger.debug("Get locale")
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    app.logger.debug('user: {}'.format(user))
    if user is not None:
        app.logger.debug('locale from user: {}'.format(user.locale))
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    if hasattr(g, 'language_code') and g.language_code is not None:
        app.logger.debug('locale from URL: {}'.format(g.language_code))
    else:
        app.logger.debug('locale from default: {}'.format(request.accept_languages.best_match(app.config['SUPPORTED_LOCALES'])))
    #return 'ja'
    #return request.accept_languages.best_match(app.config['SUPPORTED_LOCALES'])
    return getattr(g, 'language_code', request.accept_languages.best_match(app.config['SUPPORTED_LOCALES']))

@babel.timezoneselector
def get_timezone():
    app.logger.debug("Get timezone")
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

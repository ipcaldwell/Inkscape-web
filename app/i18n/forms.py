# -*- coding: utf-8 -*-

import flask.ext.wtf as wtf
from flaskext.babel import gettext as _, lazy_gettext as __
from . import db
from .model import Language

def active_languages():
    return Language.query.filter_by(is_active=True)#(Language.id, Language.name).order_by(Language.sort).all()

def language_label(language):
    return u'{} ({}-{})'.format(language.native_name, language.code, language.name)

class LanguageField(wtf.QuerySelectField):
    def __init__(self, *args, **kwargs):
        super(LanguageField, self).__init__(query_factory=active_languages, get_label=language_label, allow_blank=False, *args, **kwargs)

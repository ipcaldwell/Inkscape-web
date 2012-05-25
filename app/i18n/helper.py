# -*- encoding: utf-8 -*-

from werkzeug.routing import Rule, Submount

from app import app

def initialize_i18n():
    app.logger.debug("Initialize i18 engine")
    for rule in app.url_map._rules:
        if rule.endpoint == 'static' or rule.rule.startswith('/<string(length=2):language_code>'):
            continue
        app.logger.debug("Adding <language_code> submount to rule '{0}' with endpoint '{1}'".format(rule.rule, rule.endpoint))
        app.url_map.add(Submount('/<string(length=2):language_code>', [Rule(rule.rule, endpoint=rule.endpoint)]))


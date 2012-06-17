# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.babel import Babel
from flaskext.mail import Mail
from flask.ext.sijax import Sijax

# Flask init
app = Flask(__name__)
app.config.from_object('config')

# Internationalization
babel = Babel(app)

# Database init
db = SQLAlchemy(app)

# MySQL prior to version 5.5.5 doesn't use InnoDB by default
# Force InnoDB for all models
db.Model.__table_args__ = {'mysql_engine': 'InnoDB'}

# Login manager init
login_manager = LoginManager()
login_manager.setup_app(app)
#login_manager.anonymous_user = MyAnonymousUser

#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404

# Mail init
mail = Mail(app)

# AJAX init
Sijax(app)

# Blueprint init
from app.users.view import module as user
app.register_blueprint(user)
#app.register_blueprint(user, __name__, template_folder='templates')
login_manager.login_view = 'users.view'
#login_manager.login_message = ""

from app.i18n.view import module as i18n
app.register_blueprint(i18n)

from app.news.view import module as news
app.register_blueprint(news)

from app import view

# Complete internationalization init
from app.i18n.helper import initialize_i18n
initialize_i18n()


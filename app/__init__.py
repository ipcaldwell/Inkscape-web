# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.mail import Mail

# Flask init
app = Flask(__name__)
app.config.from_object('config')

# Database init
db = SQLAlchemy(app)

# Login manager init
login_manager = LoginManager()
login_manager.setup_app(app)
#login_manager.anonymous_user = MyAnonymousUser

#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404

# Mail init
mail = Mail(app)

# Blueprint init
from app.users.view import module as user
app.register_blueprint(user)
#app.register_blueprint(user, __name__, template_folder='templates')
login_manager.login_view = 'users.view'
#login_manager.login_message = ""

from app import view


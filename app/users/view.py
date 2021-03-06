# -*- coding: utf-8 -*-

from collections import OrderedDict as odict

from flask import Blueprint, flash, g, Markup, redirect, render_template, request, session, url_for
from flaskext.babel import gettext as _, lazy_gettext as __
from flask.ext.login import login_required, login_user, logout_user

from app import app, login_manager
from ..decorators import crumbs
from . import db, LoginForm, module, RegistrationForm, User
from . import oauth_twitter
import controller

@login_manager.unauthorized_handler
def unauthorized():
    abort(401)

@module.route('/')
@crumbs(odict((('home', __("Home")), ('.index', __("My profile")))))
def index():
    return 'USER MODULE'

@module.route('/me')
@login_required
def profile():
    return render_template('users/profile.html', user=g.user)

@app.before_request
def before_request():
    """
    Get user's profile from database before request is handled
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

#@app.after_request
#def after_request(response):
#    db.session.remove()
#    return response

@module.route('/login', methods=['GET', 'POST'])
@crumbs(odict((('home', __("Home")), ('.login', __("Login")))))
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        #user = User.query.filter_by(email=form.username.data).first()
        #app.logger.debug("Trying '{0}' as email: {1}".format(form.username.data, user))
        user = User.query.filter_by(username=form.username.data).first()
        app.logger.info("Login attempt as '{0}'".format(form.username.data))
        if user and controller.is_password_correct(user, form.password.data):
            login_user(user)
            app.logger.info("Login successful by '{}'".format(user.username))
            #session['user_id'] = user.id
            flash(_(u"Logged in as {}").format(user.username), 'success')
            #return redirect(request.referrer)
            return redirect(url_for('.profile'))
        app.logger.info("Login failed as '{}'".format(user.username))
        flash(_(u"Login failed"), 'error')
    return render_template('users/login.html', form=form)

@oauth_twitter.tokengetter
def get_twitter_token():
    return session.get('twitter_token')

@module.route('/login/twitter', methods=['GET', 'POST'])
def login_twitter():
    return oauth_twitter.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-authorized')
@oauth_twitter.authorized_handler
def oauth_authorized(response):
    next_url = request.args.get('next') or url_for('home')
    next_url = url_for('users.me')
    if response is None:
        flash(_(u"Request to sign in was denied"))
        return redirect(next_url)
    session['twitter_token'] = (response['oauth_token'], response['oauth_token_secret'])
    session['twitter_user'] = response['screen_name']
    flash(_(u"You were signed in as {}").format(response['screen_name']))
    return redirect(next_url)

@module.route('/logout')
@login_required
def logout():
    logout_user()
    #session.pop('user_id', None)
    return redirect(request.referrer)

@module.route('/register', methods=['GET', 'POST'])
@crumbs(odict((('home', __("Home")), ('.register', __("Sign up")))))
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = controller.register_user(form.username.data, form.email.data, form.password.data, form.accept_tos.data)
            if user is not None:
                flash(_(u"Thanks for registering, {}! Check your email to complete registration.").format(user.username), 'success')
                return redirect(url_for('home'))
            flash(_(u"Failed to register"), 'error')
    return render_template('users/register.html', form=form)

@module.route('/validate/<email>/<token>', methods=['GET'])
def validate(email, token):
    user = User.query.filter_by(email=email).first()
    if controller.validate_user(user, token):
        flash(_(u"You have been validated, {}").format(user.username), 'success')
    else:
        flash(_(u"I wasn't able to validate you"), 'error')
    return redirect(url_for('home'))

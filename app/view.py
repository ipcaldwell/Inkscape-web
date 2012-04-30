# -*- coding: utf-8 -*-

import os
from collections import namedtuple, OrderedDict
from functools import wraps

from flask import escape, flash, Flask, g, redirect, render_template, request, send_from_directory, session, url_for

from app import app
from app import controller as c

@app.route('/')
def home():
    # detect language from browser/ip, if nothing has ever been set. try
    # to choose best language
    app.logger.debug("Entered /")
    logged_in = False
    username = None
    if 'username' in session:
        logged_in = True
        username = session['username']
    if logged_in:
        app.logger.debug("Logged in as {0}".format(username))
    else:
        app.logger.debug("Not logged in")
    return render_template('frontpage.html', languages=app.config['LANGUAGES'])

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(403)
def error_forbidden(error):
    return render_template('403-forbidden.html'), 403

@app.errorhandler(404)
def error_page_not_found(error):
    return render_template('404-not-found.html'), 404

@app.errorhandler(500)
def error_internal_server_error(error):
    return render_template('500-internal-server-error.html'), 500

@app.route('/sitemap.xml')
def sitemap():
    url_root = request.url_root[:-1]
    rules = app.url_map.iter_rules()
    return render_template('sitemap.xml', url_root=url_root, rules=rules)

@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('users.login'))

@app.route('/logout')
def logout():
    return redirect(url_for('users.login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    return redirect(url_for('users.register'))

#@crumbs({'home': 'Home', 'about': 'About'})
#TODO: Must be an OrderedDict
@app.route('/about/')
def about():
    app.logger.debug("Entered /about")
    return render_template('about/overview.html')

@app.route('/about/features/')
def features():
    app.logger.debug("Entered /about/features")
    return render_template('about/features.html')

@app.route('/screenshots/<version>')
def screenshots():
    app.logger.debug("Entered /about/screenshots")
    return render_template('about/screenshots.html')

def crumb(hierarchy=None):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            f(*args, **kwargs)
        return wrapped
    return decorator

@app.route('/gallery/')
#@crumb({'home': 'Home', 'gallery': 'Gallery'})
def gallery():
    app.logger.debug("Entered /about/gallery")
    return render_template('about/gallery.html')

@app.route('/faq/')
def faq():
    app.logger.debug("Entered /about/faq")
    return render_template('about/faq.html')

@app.route('/testimonials/')
def testimonials():
    app.logger.debug("Entered /about/testimonials")
    return render_template('about/testimonials.html')

@app.route('/search/<query>', methods=['GET'])
def search():
    app.logger.debug("Entered /search")
    #query = request.args.get('q', '')
    if query is None:
        app.logger.debug("Empty search query")
        flash("No search terms were specified", 'error')
        if request.referrer:
            return redirect(request.referrer)
        else:
            return redirect(url_for('index'))
    else:
        query = query.strip()
        app.logger.debug("Searching for '{0}'".format(query))
        flash("Search results for '{0}'".format(query), 'success')
        #return 'Search results for <strong>{0}</strong>'.format(query)

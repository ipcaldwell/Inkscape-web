# -*- coding: utf-8 -*-

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask.ext.oauth import OAuth

from app import db
from .forms import LoginForm, RegistrationForm
from .model import User
import controller

oauth = OAuth()

oauth_twitter = oauth.remote_app('twitter',
        base_url = 'http://api.twitter.com/1/',
        request_token_url = 'https://api.twitter.com/oauth/request_token',
        access_token_url = 'https://api.twitter.com/oauth/access_token',
        authorize_url = 'https://api.twitter.com/oauth/authenticate',
        #authorize_url = 'https://api.twitter.com/oauth/authorize',
        consumer_key = '<CONSUMER_KEY>',
        consumer_secret = '<CONSUMER_SECRET>'
        )

MODULE_NAME = 'users'
MODULE_PREFIX = '/user'

module = Blueprint(MODULE_NAME, __name__, url_prefix=MODULE_PREFIX)


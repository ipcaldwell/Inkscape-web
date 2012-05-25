# -*- coding: utf-8 -*-

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.routing import Rule, Submount

from app import app, db
#from .forms import LoginForm, RegistrationForm
from .model import Language
import controller

MODULE_NAME = 'i18n'
MODULE_PREFIX = '/i18n'

module = Blueprint(MODULE_NAME, __name__, url_prefix=MODULE_PREFIX)


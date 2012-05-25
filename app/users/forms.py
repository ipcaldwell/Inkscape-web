# -*- coding: utf-8 -*-

import flask.ext.wtf as wtf
from flaskext.babel import gettext as _, lazy_gettext as __

class LoginForm(wtf.Form):
    username = wtf.TextField(__("Username"), [wtf.Required()])
    password = wtf.PasswordField(__("Password"), [wtf.Required()])

class RegistrationForm(wtf.Form):
    username = wtf.TextField(_("Username"), [wtf.Required()])
    email = wtf.html5.EmailField(__("Email"), [wtf.Required(), wtf.Email(message=__("Invalid email address")), wtf.Length(min=6, max=254, message=__("Email address must be between 6 and 254 characters long"))])
    password = wtf.PasswordField(__("Password"), [wtf.Required()])
    password2 = wtf.PasswordField(__("Password (confirm)"), [wtf.Required(), wtf.EqualTo('password', message=__("Passwords must match"))])
    accept_tos = wtf.BooleanField(__("I agree to the terms of service"), [wtf.Required()])

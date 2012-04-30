# -*- coding: utf-8 -*-

import flask.ext.wtf as wtf

class LoginForm(wtf.Form):
    username = wtf.TextField(u'Username', [wtf.Required()])
    password = wtf.PasswordField(u'Password', [wtf.Required()])

class RegistrationForm(wtf.Form):
    username = wtf.TextField(u'Username', [wtf.Required()])
    email = wtf.html5.EmailField(u'Email', [wtf.Required(), wtf.Email(message=u'Invalid email address'), wtf.Length(min=6, max=254, message=u'Email address must be between 6 and 254 characters long')])
    password = wtf.PasswordField(u'Password', [wtf.Required()])
    password2 = wtf.PasswordField(u'Password (confirm)', [wtf.Required(), wtf.EqualTo('password', message=u'Passwords must match')])
    accept_tos = wtf.BooleanField(u'I agree to the terms of service', [wtf.Required()])

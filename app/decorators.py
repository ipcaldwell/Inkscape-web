# -*- coding: utf-8 -*-

from functools import wraps

from flask import g, url_for

def crumbs(hierarchy=None, class_link=None, class_current=None):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            crumbs = []
            for item in hierarchy.keys()[:-1]:
                crumbs.append('<a href="{}"{}>{}</a>'.format(
                    url_for(item),
                    '' if class_link is None else ' class="{}"'.format(class_link),
                    hierarchy[item]))
            crumbs.append('<a{}>{}</a>'.format(
                '' if class_current is None else ' class="{}"'.format(class_current),
                hierarchy[hierarchy.keys()[-1]]))
            g.crumbs = ' &gt; '.join(crumbs)
            return f(*args, **kwargs)
        return wrapped
    return decorator



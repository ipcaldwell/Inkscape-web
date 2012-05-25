# -*- coding: utf-8 -*-
# TODO: Investigate OrderedDict.popitem(last=True)

from functools import wraps

from flask import g, url_for

def crumbs(hierarchy=None, class_link=None, class_current=None):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            crumbs = []
            for item in hierarchy.keys()[:-1]:
                crumbs.append(u'<a href="{}"{}>{}</a>'.format(
                    url_for(item),
                    u'' if class_link is None else u' class="{}"'.format(class_link),
                    unicode(hierarchy[item])))
            crumbs.append(u'<a{}>{}</a>'.format(
                u'' if class_current is None else u' class="{}"'.format(class_current),
                unicode(hierarchy[hierarchy.keys()[-1]])))
            g.crumbs = u' &gt; '.join(crumbs)
            return f(*args, **kwargs)
        return wrapped
    return decorator



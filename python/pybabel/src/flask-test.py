# coding: utf-8
# as per http://www.python.org/dev/peps/pep-0263/

from flask import Flask, g, render_template, request, _request_ctx_stack
app = Flask(__name__)
app.debug = True

from flask.ext.babel import Babel, gettext
babel = Babel(app)

from datetime import datetime
from functools import wraps

LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

def setlocale(f):
    @wraps(f)
    def new_f(*args, **kwargs):
        lang = request.args.get('lang', None)
        if lang is not None:
            ctx = _request_ctx_stack.top
            ctx.babel_locale = lang
        return f(*args, **kwargs)
    return new_f


@app.route('/')
@setlocale
def hello_world():
    return gettext('Hello') + ' Simon ' + str(datetime.now().time().strftime('%H:%M:%S'))

@app.route('/hello')
@setlocale
def hello():
    return render_template('index.html')


@babel.localeselector
def get_locale():
    #user = getattr(g, 'user', None)
    #if user is not None:
    #    return user.locale
    return request.accept_languages.best_match(LANGUAGES.keys())


if __name__ == '__main__':
    app.run()

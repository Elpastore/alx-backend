#!/usr/bin/env python3
"""
0-app module
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
# The `_` function is a shorthand for the gettext function,
# used to mark strings for translation


class Config():
    """
    babel  config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask("__name__")
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    get_locale function
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    """
    the index page
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

#!/usr/bin/env python3
"""
0-app module
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


# @babel.localeselector
def get_locale():
    """
    get_locale function
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    the index page
    """
    locale = get_locale()
    return render_template('3-index.html', locale=locale)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

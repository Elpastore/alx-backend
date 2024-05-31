#!/usr/bin/env python3
"""
0-app module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from pytz import timezone
# The `_` function is a shorthand for the gettext function,
# used to mark strings for translation


class Config():
    """
    babel  config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# app config
app = Flask("__name__")
app.config.from_object(Config)
babel = Babel(app)

# users mock database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    get_locale function
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.init_app(app, locale_selector=get_locale)


@babel.timezoneselector
def get_timezone():
    """
    get_timezone function
    """
    timeZone = request.args.get('timezone')
    if timeZone:
        try:
            return timezone(timeZone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            timeZone = g.user.get('timezone')
            return timezone(timeZone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    default_timezone = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_timezone


def get_user():
    """
    return a user dict
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    """
    user = get_user()
    g.user = user


@app.route('/')
def home():
    """
    the index page
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

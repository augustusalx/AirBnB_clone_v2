#!/usr/bin/python3
"""The script to start a flask app on localhost
"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(exc=None):
    """called on teardown of app contexts,
        for more info on contexts visit
        -> http://flask.pocoo.org/docs/1.0/appcontext/

        Storage.close() closes the sql scoped session or reloads file
            storage.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def conditional_templating(n=None):
    """To check input data using templating"""
    states = storage.all("State")
    data = {}
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
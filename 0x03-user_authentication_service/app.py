#!/usr/bin/env python3
"""
In this task, you will set up a basic Flask app.
Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload of the form:
"""

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def route():
    """
    returns a JSON payload of the form
    """
    form = {
        "message": "Bienvenue"
    }

    return jsonify(form)


if __name__ == '__main__':
    app.run(debug=True)

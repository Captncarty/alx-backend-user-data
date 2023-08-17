#!/usr/bin/env python3
"""
In this task, you will set up a basic Flask app.
Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload of the form:
"""

from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
auth = Auth()


@app.route('/', methods=['GET'])
def route() -> str:
    """
    returns a JSON payload of the form
    """
    form = {
        "message": "Bienvenue"
    }

    return jsonify(form)


@app.route('/users', methods=['POST'])
def users() -> str:
    """
    implement the end-point to register a user
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        new_user = auth.register_user(email, password)
        if new_user is not None:
            return jsonify({
                "email": new_user.email,
                "message": "user created"
                })
    except ValueError:
        return jsonify({
            "message": "email already registered"
            }), 400
    return None


if __name__ == '__main__':
    app.run(debug=True)

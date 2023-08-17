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

@app.route('/profile', methods=['GET']
def profile() -> str:
    """
    implement a profile function to respond to the
    GET /profile route
    Expected to contain a session_id cookie
    Use it to find the user. If the user exist,
    respond with a 200 HTTP status and
    the following JSON payload:
    If the session ID is invalid
    or
    the user does not exist,
    respond with a 403 HTTP status.
    """
    session_id = request.cookies.get("session_id", None)
    user = auth.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    return jsonify({"email": user.email}), 200
    
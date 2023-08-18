#!/usr/bin/env python3
"""
In this task, you will set up a basic Flask app.
Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload of the form:
"""

from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['POST'])
def sessions() -> str:
    """
    Expected to contain form data with "email" and a "password" fields.
    If the login information is incorrect;
    use flask.abort to respond with a 401 HTTP status.
    Otherwise,
    create a new session for the user,
    store it the session ID as a cookie with key "session_id"
    on the response and return a JSON payload of the form
    """
    email = request.form.get('email')
    password = request.form.get('password')

    login = auth.valid_login(email, password)
    if not login:
        abort(401)
    session_id = auth.create_session(email)
    message = {"email": email, "message": "logged in"}
    response = jsonify(message)
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """
           Implement a logout function to respond to the DELETE
           /sessions route.
           Expected to contain the session ID as a cookie with key "session_id"
           Find the user with the requested session ID.
           If the user exists destroy the session and redirect the
           user to GET /
           If the user does not exist, respond with a 403 HTTP status.
     """
    cookie = request.cookies.get("session_id", None)
    user = auth.get_user_from_session_id(cookie)

    if cookie is None or user is None:
        abort(403)
    auth.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ GET /profile
    Return:
        - Use session_id to find the user.
        - 403 if session ID is invalid
    """
    user_cookie = request.cookies.get("session_id", None)
    if user_cookie is None:
        abort(403)
    user = auth.get_user_from_session_id(user_cookie)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ POST /reset_password
            - email
        Return:
            - Generate a Token
            - 403 if email not registered
    """
    user_request = request.form
    user_email = user_request.get('email')
    is_registered = auth.create_session(user_email)

    if not is_registered:
        abort(403)

    token = auth.get_reset_password_token(user_email)
    message = {"email": user_email, "reset_token": token}
    return jsonify(message)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ PUT /reset_password
            - email
            - reset_token
            - new_password
        Return:
            - Update the password
            - 403 if token is invalid
    """
    user_email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        auth.update_password(reset_token, new_password)
    except Exception:
        abort(403)

    message = {"email": user_email, "message": "Password updated"}
    return jsonify(message), 200


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python3
"""
giving http methods a try:
    GET
    POST
    PUT
    DELETE
"""


from flask import Flask, request

app = Flask(__name__)

def do_the_login():
    # Simulated login logic
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return 'Logged in successfully'
    else:
        return 'Login failed'

def show_the_login_form():
    # Simulated login form rendering logic
    return """
    <form method="post">
        <input type="text" name="username" placeholder="Username"><br>
        <input type="password" name="password" placeholder="Password"><br>
        <input type="submit" value="Log In">
    </form>
    """

@app.route('/', methods=['GET', 'POST'])
def get_route():
    """
    using GET and POST
    """
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True)

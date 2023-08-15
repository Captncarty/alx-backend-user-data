#!/usr/bin/env python3
"""
running test cases
"""


import flask
from markupsafe import escape

"""
import Flask
"""

app = flask.Flask(__name__)

@app.route('/')
def route():
    return 'Hello world/n'

@app.route('/json')
def new_route():
    new_r = {
            'name': 'anthony',
            'newton': [],
            'more': {
                'name': 'handsom',
                'city': 'newhampson',
                'friends': []
                },
            'new_list': [1,2,3,4,5,6]
        }
    return new_r

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

if __name__ == '__main__':
    app.run(debug=True)


#!/usr/bin/env python3
"""
initiating flask-login
"""

from flask import Flask, request
from flask-login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()



import os
from flask import Flask
from flask_login import LoginManager

# Initialize application
app = Flask(__name__, static_folder='static')
login_manager = LoginManager(app)

# Import the application views
from bringmfapp import bring_my_food

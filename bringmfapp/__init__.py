import os
from flask import Flask

# Initialize application
app = Flask(__name__, static_folder='static')

# Import the application views
from bringmfapp import bring_my_food
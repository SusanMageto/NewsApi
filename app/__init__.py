from flask import Flask

#initializing our app
app = Flask(__name__)

from app import views

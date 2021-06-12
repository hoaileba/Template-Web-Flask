from flask import Flask, render_template
import os
import json
from .Pages.page import appbp
import time
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_pyfile('settings.py')
    app.register_blueprint(appbp)
    return app

app  = create_app()
    

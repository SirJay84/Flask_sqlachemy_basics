from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myapp.main.config import app_config
from myapp.main.commands import create_database



db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.cli.add_command(create_database)
    db.init_app(app)

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager



login_Manager = login_Manager()
login_manager.session_protection = 'strong'


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    db.init_app(app)
    login_Manager.init_app(app)



    #Registering the blueprint 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
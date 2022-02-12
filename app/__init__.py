from ensurepip import bootstrap
import imp
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #initialize extensions
    bootstrap.init_app(app)

    # register blueprint
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
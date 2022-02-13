from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_simplemde import SimpleMDE

bootstrap = Bootstrap()
simple = SimpleMDE()

def create_app(config_name):

    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #initialize extensions
    bootstrap.init_app(app)
    simple.init_app(app)

    # register blueprint
    from .main import main as main_blueprint
    from . auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
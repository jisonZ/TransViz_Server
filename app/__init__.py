from flask import Flask
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
import os
# blueprints
from app.errors.handlers import errors
from app.home.routes import home
from app.utils.routes import utils
from app.components.routes import components, component_init

# import db and models
from .extensions import db
from .entities.models import *

# app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)

# app.register_blueprint(errors)
# app.register_blueprint(home)
# app.register_blueprint(utils)
# app.register_blueprint(components)

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # app.config.from_object(DevelopmentConfig if os.environ.get(
    #     "PRODUCTION").lower() == 'true' else DevelopmentConfig)
    
    app.register_blueprint(errors)
    app.register_blueprint(home)
    app.register_blueprint(utils)
    app.register_blueprint(components)

    # initialize
    component_init()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

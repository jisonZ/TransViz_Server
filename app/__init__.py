from flask import Flask
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
import os
# blueprints
from app.errors.handlers import errors
from app.home.routes import home
from app.utils.routes import utils
from app.components.routes import components, component_init
from app.modelflow.routes import model 

# import db and models
from .extensions import db
from .entities.models import *
from flask_cors import CORS, cross_origin

# app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)

# app.register_blueprint(errors)
# app.register_blueprint(home)
# app.register_blueprint(utils)
# app.register_blueprint(components)

def create_app(database_uri='sqlite:///db.sqlite3'):
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_object(DevelopmentConfig)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    db.init_app(app)

    # app.config.from_object(DevelopmentConfig if os.environ.get(
    #     "PRODUCTION").lower() == 'true' else DevelopmentConfig)
    
    app.register_blueprint(errors)
    app.register_blueprint(home)
    app.register_blueprint(utils)
    app.register_blueprint(components)
    app.register_blueprint(model)

    # initialize
    component_init()
    
    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app

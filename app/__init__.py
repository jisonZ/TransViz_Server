from flask import Flask
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
import os
# blueprints
from app.errors.handlers import errors
from app.home.routes import home
from app.utils.routes import utils
from app.components.routes import components, component_init

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(errors)
app.register_blueprint(home)
app.register_blueprint(utils)
app.register_blueprint(components)

# initialize
data = []
component_init()

# def create_app():
#     app.logger.info("Creating app")
#     app = Flask(__name__)
#     app.config.from_object(DevelopmentConfig if os.environ.get(
#         "PRODUCTION").lower() == 'true' else DevelopmentConfig)
#     init_app()
#     return app

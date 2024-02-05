from app.extensions import db
from app import create_app
from app.entities import *

database_uri='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

with app.app_context():
    db.create_all()
    print('Database created')
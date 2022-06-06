from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')

ma = Marshmallow(app)
db = SQLAlchemy(app)

CORS(app)

from app.models.aeroporto import Aeroporto
db.create_all()

from app.controllers import *




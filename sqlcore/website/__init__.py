from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app =  Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'd4c516c7e3b267a33db6a317ffab126b1bc85ccc2d4d2b2fd5e169c34877'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@localhost/myflaskproject'

db = SQLAlchemy(app)
ma = Marshmallow(app)

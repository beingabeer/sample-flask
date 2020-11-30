from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

# Initialization and setup
app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, db.sqlite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/')
def homepage():
    return "<h1>This is the homepage</h1>"


# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer, default=1)

    # def __init__(self, name, description, price, quantity):
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity

    def __repr__(self):
        return f"Product({self.name})"


# Run server
if __name__ == "__main__":
    app.run(debug=True)





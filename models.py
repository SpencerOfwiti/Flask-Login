from flask_login import UserMixin
from .__init__ import db


class User(UserMixin, db.Model):
    """
    Creating a User object
    """
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

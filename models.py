"""Models for inventory app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    """model for item in inventory"""

    __tablename__ = "items"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    warehouse = db.Column(db.Text, db.ForeignKey('warehouses.name'))

class Warehouse(db.Model):
    """model for warehouse"""

    __tablename__ = "warehouses"

    name = db.Column(db.Text, nullable=False, primary_key=True)
   
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
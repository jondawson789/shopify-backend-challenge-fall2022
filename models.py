"""Models for inventory app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    """model for item in inventory"""

    __tablename__ = "items"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'))

    warehouse = db.relationship('Warehouse', backref='items')

class Warehouse(db.Model):
    """model for warehouse"""

    __tablename__ = "warehouses"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
   
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
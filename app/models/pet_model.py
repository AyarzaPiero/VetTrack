from ..db import db
from datetime import datetime

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=True)
    breed = db.Column(db.String(100), nullable=True)
    age = db.Column(db.Float, nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    color = db.Column(db.String(50), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    vaccinated = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Pet {self.name}>"
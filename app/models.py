from datetime import datetime
from . import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    initials = db.Column(db.String(4), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(20), nullable=False)
    reports_to = db.Column(db.Integer, nullable=True)
    join_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Employee('{self.type}', '{self.size}', '{self.id}')"

class Drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(2), nullable=False)
    size = db.Column(db.String(1), nullable=False)
    drawn = db.Column(db.String(20), nullable=False)
    drawn_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    checked = db.Column(db.String(20), nullable=True)
    checked_date = db.Column(db.Date, nullable=True)
    approved = db.Column(db.String(20), nullable=True)
    approved_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"Drawing('{self.type}', '{self.size}', '{self.id}')"



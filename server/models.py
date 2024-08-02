from flask_sqlalchemy import SQLAlchemy
from bcrypt import gensalt, hashpw, checkpw
from config import db

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    tickets = db.relationship('Ticket', backref='user', lazy=True)
    concerts = db.relationship('ConcertUser', back_populates='user')

    def set_password(self, password):
        self.password_hash = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

# Concert Model with Image
class Concert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    venue = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)  # Field for image URL
    tickets = db.relationship('Ticket', backref='concert', lazy=True)
    attendees = db.relationship('ConcertUser', back_populates='concert')

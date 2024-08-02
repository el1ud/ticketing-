# !/usr/bin/env python3

# Standard library imports

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_restful import Api, Resource

# Local imports
from config import Config
from models import db, User, Ticket, Concert, ConcertUser

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)

# User Routes
class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })
    
    @jwt_required()
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

# Concert Routes
class ConcertResource(Resource):
    def get(self, concert_id):
        concert = Concert.query.get_or_404(concert_id)
        return jsonify({
            "id": concert.id,
            "name": concert.name,
            "date": concert.date.isoformat(),
            "venue": concert.venue,
            "image_url": concert.image_url
        })

# Ticket Routes
class TicketResource(Resource):
    def get(self, ticket_id):
        ticket = Ticket.query.get_or_404(ticket_id)
        return jsonify({
            "id": ticket.id,
            "seat_number": ticket.seat_number,
            "price": ticket.price,
            "user_id": ticket.user_id,
            "concert_id": ticket.concert_id
        })

# Auth Routes
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400

    user = User(
        username=data['username'],
        email=data['email'],
        password_hash=bcrypt.generate_password_hash(data['password']).decode('utf-8')
    )
    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 201

# Register API routes
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(ConcertResource, '/concerts/<int:concert_id>')
api.add_resource(TicketResource, '/tickets/<int:ticket_id>')

# Additional app configuration if needed

if __name__ == '__main__':
    app.run(debug=True)

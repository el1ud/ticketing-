# #!/usr/bin/env python3

# # Standard library imports

# # Remote library imports
# from flask import request
# from flask_restful import Resource

# # Local imports
# from config import app, db, api
# # Add your model imports


# # Views go here!

# # @app.route('/')
# # def index():
# #     return '<h1>Project Server</h1>'


# # @app.route("/members")
# # def index():
# #     return {"members": ["Members1", "Members2", "Members3"]}


# # if __name__ == '__main__':
# #     app.run(port=5555, debug=True)

# #!/usr/bin/env python3

# # Standard library imports

# # Remote library imports
# from flask import request, make_response, send_from_directory, session
# from flask_restful import Resource
# import os


# # Local imports
# from server.config import app, db, api
# # Add your model imports
# from server.models import db, User, Destination, Review


# @app.route('/')
# def index():
#     return '<h1>Wanderers</h1>'
# class Users(Resource):
    
#     def get(self):
#         users = [user.to_dict() for user in User.query.all()]
#         return make_response(users, 200)

# class UserByID(Resource):   
    
#     def get(self, id):
#         user = User.query.filter_by(id=id).first()
        
#         if user:
#             return make_response(user.to_dict(), 200)
        
#         return make_response({'error': 'User not found'}, 404)
    
#     def delete(self, id):
#         user = User.query.filter_by(id= id).first()
#         if user:
#             db.session.delete(user)
#             db.session.commit()
#             return make_response({}, 204)
#         else:
#             return make_response({'error': 'User not found'}, 404)
        
#     def patch(self, id):
#         user = User.query.filter_by(id= id).first()
#         if user:
#             try:
#                 for attr in request.json:
#                     setattr(user, attr, request.json[attr])
#                 db.session.add(user)
#                 db.session.commit()
#                 return make_response(user.to_dict(), 200)
#             except ValueError as e:
#                 return make_response({'error': str(e)}, 400)
#         else:
#             return make_response({'error': 'User not found'}, 404)
    
# class Destinations(Resource):
    
#     def get(self):
#         destinations = [destination.to_dict() for destination in Destination.query.all()]
#         return make_response(destinations, 200)
    
#     def post(self):
#         try:
#             destination = Destination(name=request.form.get('name'), location=request.form.get('location'), description=request.form.get('description'), image=request.form.get('link'), link=request.form.get('link'))
#             db.session.add(destination)
#             db.session.commit()
#             return make_response(destination.to_dict(), 201)
#         except ValueError as e:
#             return make_response({'error': str(e)}, 400)
    
# class DestinationByID(Resource):
    
#     def get(self,id):
#         destination = Destination.query.filter_by(id=id).first()
        
#         if destination:
#             return make_response(destination.to_dict(), 200)
        
#         return make_response({'error': 'Destination not found'}, 404)
    
#     def delete(self, id):
#         destination = Destination.query.filter_by(id= id).first()
#         if destination:
#             db.session.delete(destination)
#             db.session.commit()
#             return make_response({}, 204)
#         else:
#             return make_response({'error': 'Destination not found'}, 404)
        
#     def patch(self, id):
#         destination = Destination.query.filter_by(id=id).first()
#         if destination:
#             try:
#                 for attr in request.json:
#                     setattr(destination, attr, request.json[attr])
            
#                 db.session.add(destination)
#                 db.session.commit()
#                 return make_response(destination.to_dict(), 200)
#             except ValueError as e:
#                 return make_response({'error': str(e)}, 400)
#         else:
#             return make_response({'error': 'Destination not found'}, 404)
      
# ### Route for images ###
# @app.route('/api/static/uploads/<filename>')
# def uploads(filename):
#     return send_from_directory('uploads', filename)
    
# class Reviews(Resource):
    
#     def get(self):
#         reviews = [review.to_dict() for review in Review.query.all()]
#         return make_response(reviews, 200)
    
#     def post(self):
#             data = request.json
#             if session['user_id']:
#                 try:
#                     review = Review(user_id=session['user_id'], destination_id=data['destination_id'], rating=data['rating'], comment=data['comment'])
#                     db.session.add(review)
#                     db.session.commit()
#                     return make_response(review.to_dict(), 201)
#                 except ValueError as e:
#                     print(e)
#                     return make_response({'error': str(e)}, 400)

#             else:
#                 return make_response({'error': 'You need to be logged in to post a review'}, 401)

# class ReviewByID(Resource):
    
#     def get(self, id):
#         review = Review.query.filter_by(id=id).first()
        
#         if review:
#             return make_response(review.to_dict(), 200)
        
#         return make_response({'error': 'Review not found'}, 404)
    
#     def delete(self, id):
#         review = Review.query.filter_by(id= id).first()
#         if review:
#             db.session.delete(review)
#             db.session.commit()
#             return make_response({}, 204)
#         else:
#             return make_response({'error': 'Review not found'}, 404)
        
#     def patch(self, id):
#         review = Review.query.filter_by(id=id).first()
#         if review:
#             try:
#                 for attr in request.json:
#                     setattr(review, attr, request.json[attr])
#                 db.session.add(review)
#                 db.session.commit()
#                 return make_response(review.to_dict(), 200)
#             except ValueError as e:
#                 return make_response({'error': str(e)}, 400)
      
# class Login(Resource):
    
#     def post(self):
#         username = request.json.get('username')
#         user = User.query.filter_by(username=username).first()
#         password = request.json.get('password')
#         if user:
#             if user.authenticate(password):
#                 session['user_id'] = user.id
#                 return user.to_dict(), 200
#             else:
#                 return make_response({'error': 'Incorrect password'}, 401)
#         else:
#             return {'error': 'User not found'}, 404
        
# class Logout(Resource):
    
#     def delete(self):
#         session['user_id'] = None
#         return {'message': 'Logged out successfully'}, 204
    
    
# class Register(Resource):
#     def post(self):
#         data = request.get_json()
#         try:
#             user = User(username=data['username'].title(), email=data['email'], password=data['password'])
#             db.session.add(user)
#             db.session.commit()
#             session['user_id'] = user.id
#             return make_response(user.to_dict(), 201)
#         except ValueError as e:
#             return make_response({'error': str(e)}, 400)
        
# class CheckSession(Resource):
    
#     def get(self):
#         user_id = session.get('user_id')
#         print(user_id)
#         user = User.query.filter_by(id=user_id).first()
#         if user:
#             return make_response(user.to_dict(), 200)
#         else:
#             return {'error': 'Session expired'}, 401
    
    
# api.add_resource(Users, '/api/users')
# api.add_resource(Destinations, '/api/destinations')
# api.add_resource(Reviews, '/api/reviews')
# api.add_resource(UserByID, '/api/users/<int:id>')
# api.add_resource(DestinationByID, '/api/destinations/<int:id>')
# api.add_resource(ReviewByID, '/api/reviews/<int:id>')
# api.add_resource(Login, '/api/login')
# api.add_resource(Logout, '/api/logout')
# api.add_resource(CheckSession, '/api/check-session')
# api.add_resource(Register, '/api/register')
    

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from config import  app, db
# from flask_migrate import Migrate 
# from models import db, User,Ticket, Concert, ConcertUser


# app = Flask(__name__)
# # app.config.from_object(Config)
# db = SQLAlchemy(app)
# db.init_app(app)
# migrate = Migrate(app, db)
# # Other configurations or route definitions


# Remote library imports
# from flask import request, jsonify
# from flask_restful import Resource
# from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import jwt_manager, create_access_token, jwt_required, get_jwt_identity

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager
# from flask_restful import Api

# # Local imports
# from config import app, db, api

# # Add your model imports
# from models import db, User,Ticket, Concert, ConcertUser



# db.init_app(app)
# migrate = Migrate(app, db)


# from flask import Flask, jsonify, abort, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager
# from flask_restful import Api

# # Local imports
# from config import Config
# from models import db, User, Ticket, Concert, ConcertUser
# from app import initialize_routes  # Assuming routes are defined in routes.py

# # Initialize Flask app
# app = Flask(__name__)
# app.config.from_object(Config)

# # Initialize extensions
# db.init_app(app)
# migrate = Migrate(app, db)
# bcrypt = Bcrypt(app)
# jwt = JWTManager(app)
# api = Api(app)

# # Initialize routes
# initialize_routes(api)

# # Additional app configuration if needed

# if __name__ == '__main__':
#     app.run(debug=True)


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

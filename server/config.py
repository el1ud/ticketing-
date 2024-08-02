# # # Standard library imports

# # # Remote library imports
# # from flask import Flask
# # from flask_cors import CORS
# # from flask_migrate import Migrate
# # from flask_restful import Api
# # from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy import MetaData

# # # Local imports

# # # Instantiate app, set attributes
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.json.compact = False

# # # Define metadata, instantiate db
# # metadata = MetaData(naming_convention={
# #     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# # })
# # db = SQLAlchemy(metadata=metadata)
# # migrate = Migrate(app, db)
# # db.init_app(app)

# # # Instantiate REST API
# # api = Api(app)

# # # Instantiate CORS
# # CORS(app)


# # Standard library imports

# # Remote library imports
# from flask import Flask, session
# from flask_cors import CORS
# from flask_migrate import Migrate
# from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from flask_bcrypt import Bcrypt
# from flask_session import Session
# import os

# # Local imports
# UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'server/uploads')

# # Instantiate app, set attributes
# app = Flask(__name__)
# app.secret_key = b'/O\xf5\xa8\xf1\xc5\x97\xdcM\xcc\xd0\xf0\xf4\r\xc7f'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config["SESSION_COOKIE_SAMESITE"] = "None"
# app.config["SESSION_COOKIE_SECURE"] = True
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

# #redis_url = os.environ.get('REDIS_URL')
# app.config['SESSION_TYPE'] = 'redis'
# #app.config['SESSION_REDIS'] = redis.from_url(redis_url)
# app.config['SESSION_USE_SIGNER'] = True
# app.config['SESSION_PERMANENT'] = False


# app.json.compact = False

# # Define metadata, instantiate db
# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })
# db = SQLAlchemy(metadata=metadata)
# migrate = Migrate(app, db)
# db.init_app(app)
# app.config['SESSION_SQLALCHEMY'] = db


# bcrypt = Bcrypt(app)

# # Instantiate REST API
# api = Api(app)
# Session(app)

# # Instantiate CORS
# CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}},)
# import os

# class Config:
#     # Replace the following with your actual database URI
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///your_database.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

 #Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Local imports

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key_here'
app.json.compact = False

# config.py

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # For JWT authentication


# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
# migrate = Migrate(app, db)
# db.init_app(app)

# Instantiate REST API
api = Api(app)

# Instantiate CORS
CORS(app)

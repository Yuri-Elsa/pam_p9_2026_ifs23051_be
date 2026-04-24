from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Shared extensions used across app, models, and routes.
db = SQLAlchemy()
jwt = JWTManager()

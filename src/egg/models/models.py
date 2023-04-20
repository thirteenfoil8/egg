import jwt
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class WebCounter:
    def __init__(self, id, new_value, last_value, updated_at):
        self.id = id
        self.new_value = new_value
        self.last_value = last_value
        self.updated_at = updated_at

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
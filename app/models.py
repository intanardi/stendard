from app import create_app, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(128))
    created_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

    
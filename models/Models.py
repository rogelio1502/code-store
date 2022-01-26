from email.policy import default
from . import db
from .base_model import Base
from models import base_model

class Article(db.Model,Base):

    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey('categories.id'),
        nullable=False
    )
    added_by = db.Column(
        db.Integer, db.ForeignKey('user.id'),
        nullable=False, default=4
    )
    db.UniqueConstraint(name)    
    
class Category(db.Model,Base):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    status = db.Column(db.Boolean, default=1, server_default="1", nullable=False)
    articles = db.relationship(
        'Article',backref="category", lazy=True
    )
    added_by = db.Column(
        db.Integer, db.ForeignKey('user.id'),
        nullable=True, default=4, server_default="4"
    )
    db.UniqueConstraint(name)

class User(db.Model, Base):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(150), unique = True)
    name = db.Column(db.String(75), nullable=False)
    last_name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(70), unique = True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(10), nullable=True)
    status = db.Column(
        db.String(10),default="active",
             server_default="active", nullable=False
    )
    
    articles = db.relationship(
        'Article',backref="user", lazy=True
    )
    categories = db.relationship(
        'Category',backref="user", lazy=True
    )

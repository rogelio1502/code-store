from . import db
from .base_model import Base

class Article(db.Model,Base):

    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey('categories.id'),
        nullable=False
    )
    db.UniqueConstraint(name)    
    
class Category(db.Model,Base):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    articles = db.relationship(
        'Article',backref="category", lazy=True
    )
    db.UniqueConstraint(name)

    
from . import db

class Article(db.Model):

    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price' : self.id
        }
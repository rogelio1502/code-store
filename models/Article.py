from curses import noecho
from utils.Exceptions import BadRequestException
from . import db

class Article(db.Model):

    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    db.UniqueConstraint(name)    
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price' : self.price
        }
    
    @classmethod
    def get_all_articles(_class):

        articles_obj = _class.query.all()
        articles_json = []

        for i in articles_obj:
            articles_json.append(i.serialize)

        return articles_json
    
    @classmethod
    def insert_article(self,data):
        
        obj = self()
        for i in data:
            setattr(obj, i, data[i])
        db.session.add(obj)
        db.session.commit()
        
    
        return obj.serialize
    
    @classmethod
    def remove_article(self,id):
        obj = self()
        article = obj.query.filter_by(id=id).first()

        print(article.serialize)

        try:
            db.session.delete(article)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise BadRequestException(str(e))
        else:
            return True

    @classmethod 
    def update_article(self, data):
        
        obj = self()

        try:
            article = obj.query.filter_by(id=data['id']).first()
            if article is not None:

                for i in data:
                    if i != "id":
                        setattr(article, i, data[i])
            else:
                raise BadRequestException(f"Does not exist a row with id {data['id']}")

        except Exception as e:
            raise BadRequestException(str(e))

        try:
            db.session.commit()
        except Exception as e:
            raise BadRequestException(str(e))
        return article.serialize

    @classmethod
    def get_article(self, id):
        obj = self()

        article = obj.query.filter_by(id=id).first()

        if article is not None:
            return article.serialize
        return {}

    
from .Models import Article
from .CategoryModel import CategoryModel

class ArticleModel(Article):

    @property
    def serialize(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'price' : self.price,
            'category' : CategoryModel.get_category_by_id(self.category_id)
        }

    def get_all_articles():
        results = ArticleModel.get_all()
        
        return results
    
    def insert_article(data):
        response = ArticleModel.insert(data)
        return response
    
    def delete_article(id):
        response = ArticleModel.delete(id)
        return response

    def update_article(data):
        response = ArticleModel.update(data)
        return response
        
    def get_article(id):
        data = ArticleModel.get(id)
        return data
    
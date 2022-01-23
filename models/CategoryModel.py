from flask import jsonify
from .Models import Category

class CategoryModel(Category):

    @property
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "status": "Active" if self.status else "Inactive"
        }

    def get_all_categories():

        data = CategoryModel.get_all()

        return data

    def insert_category(data):
        data = CategoryModel.insert(data)
        return data

    def get_category_by_id(id):
        data = CategoryModel.get(id)
        return data
    

    def update_category(data):
        response = CategoryModel.update(data)
        return response

    def disable_category(id):
        data = {
            "id" : id,
            "status" : False
        }
        response = CategoryModel.update(data)
        return response
    




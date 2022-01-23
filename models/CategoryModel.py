from .Models import Category

class CategoryModel(Category):

    @property
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name
        }

    def insert_category(data):
        data = CategoryModel.insert(data)
        return data

    def get_category_by_id(id):
        data = CategoryModel.get(id)
        return data



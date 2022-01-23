from flask import request, jsonify
from models.CategoryModel import CategoryModel

def store():
    data = request.get_json()
    response = CategoryModel.insert_category(data)
    return jsonify(response)

def show_all():
    data = CategoryModel.get_all_categories()
    return jsonify(data)


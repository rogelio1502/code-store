from flask import request, jsonify
from models.CategoryModel import CategoryModel

def store():
    data = request.get_json()
    response = CategoryModel.insert_category(data)
    return jsonify(response)

def show_all():
    data = CategoryModel.get_all_categories()
    return jsonify(data)

def show(id):

    data = CategoryModel.get_category_by_id(id)
    return jsonify(data)

def update():
    data = request.get_json()
    response = CategoryModel.update_category(data)
    return jsonify(response)

def disable():
    id = request.get_json()["id"]

    done = CategoryModel.disable_category(id)
    return {
        "status":done
    }

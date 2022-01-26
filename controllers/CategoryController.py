from flask import request, jsonify
from models.CategoryModel import CategoryModel
from utils.JwtToken import token_required

@token_required
def store(current_user):
    data = request.get_json()
    response = CategoryModel.insert_category(data)
    return jsonify(response)

def show_all():
    data = CategoryModel.get_all_categories()
    return jsonify(data)


def show(id):

    data = CategoryModel.get_category_by_id(id)
    return jsonify(data)

@token_required
def update(current_user):
    data = request.get_json()
    response = CategoryModel.update_category(data)
    return jsonify(response)

@token_required
def disable(current_user):
    id = request.get_json()["id"]

    done = CategoryModel.disable_category(id)
    return {
        "status":done
    }

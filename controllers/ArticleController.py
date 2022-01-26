from flask import request, jsonify
from models.ArticleModel import ArticleModel
from utils.JwtToken import token_required

@token_required
def store(current_user):
    data = request.get_json()
    response = ArticleModel.insert_article(data)
        
    return response

def show_all():
    
    data = ArticleModel.get_all_articles()
    
    return jsonify(data)

@token_required
def delete(current_user):

    id = request.get_json()["id"]

    done = ArticleModel.delete_article(id)

    return {
        "status":done
    }
@token_required
def update(current_user):

    data = request.get_json()

    response = ArticleModel.update_article(data)

    return response

def show(id):

    data = ArticleModel.get_article(id)

    return data

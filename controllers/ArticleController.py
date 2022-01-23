from flask import request, jsonify
from models.ArticleModel import ArticleModel


def store():
    data = request.get_json()
    response = ArticleModel.insert_article(data)
        
    return response

def show_all():
    
    data = ArticleModel.get_all_articles()
    
    return jsonify(data)

def delete():

    id = request.get_json()["id"]

    done = ArticleModel.delete_article(id)

    return {
        "status":done
    }

def update():

    data = request.get_json()

    response = ArticleModel.update_article(data)

    return response

def show(id):

    data = ArticleModel.get_article(id)

    return data

from flask import request, jsonify
from models.Article import Article


def store():
    data = request.get_json()
    response = Article.insert_article(data)
        
    return response

def show_all():
    
    data = Article.get_all_articles()
    
    return jsonify(data)

def delete():

    id = request.get_json()["id"]

    done = Article.remove_article(id)

    return {
        "status":done
    }

def update():

    data = request.get_json()

    response = Article.update_article(data)

    return response

def show(id):

    data = Article.get_article(id)

    return data

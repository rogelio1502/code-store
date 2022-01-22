# import sys
# from flask import render_template, redirect, url_for, request, abort
# from models.model import SomeModel

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

# def index():

#     return render_template('controller/index.html')
# def store():
#     data = request.get_json()
#     new_model = SomeModel()
#     for i in data:
#         setattr(new_model, i, data[i])
#     db.session.add(new_model)
#     db.session.commit()
    
#     return redirect(url_for('index'))
# def show(module_id):
#     pass
# def update(module_id):
#     pass
# def delete(userId):
#     pass

from flask import Flask, request, redirect, url_for
from models import db
from models.Store import Article


def index():

    return {
        "message" : "Hello World"
    }
def store():
    data = request.get_json()
    new_model = Article()
    for i in data:
        setattr(new_model, i, data[i])
    db.session.add(new_model)
    db.session.commit()
    return redirect(url_for('index'))
from flask import Blueprint

from controllers.CategoryController import store

category = Blueprint('category', __name__)


#article.route('/get-all', methods=['GET'])(show_all)
category.route('/store', methods=['POST'])(store)
#article.route('/<int:id>', methods=['GET'])(show)#
#article.route('/update', methods=['PUT'])(update)
#article.route('/delete', methods=['DELETE'])(delete)
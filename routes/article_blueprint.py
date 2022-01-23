from flask import Blueprint

from controllers.ArticleController import delete, store, show_all,update, show

article = Blueprint('article', __name__)


article.route('/get-all', methods=['GET'])(show_all)
article.route('/store', methods=['POST'])(store)
article.route('/<int:id>', methods=['GET'])(show)
article.route('/update', methods=['PUT'])(update)
article.route('/delete', methods=['DELETE'])(delete)
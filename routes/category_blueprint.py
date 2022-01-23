from dis import dis
from flask import Blueprint

from controllers.CategoryController import store, show_all,show, update, disable

category = Blueprint('category', __name__)


category.route('/get-all', methods=['GET'])(show_all)
category.route('/store', methods=['POST'])(store)
category.route('/<int:id>', methods=['GET'])(show)
category.route('/update', methods=['PUT'])(update)
category.route('/delete', methods=['DELETE'])(disable)
from flask import Blueprint

from controllers.StoreController import index,store

storebp = Blueprint('store', __name__)


storebp.route('/', methods=['GET'])(index)
storebp.route('/create', methods=['POST'])(store)
# mp.route('/<int:model_id>', methods=['GET'])(show)
# mp.route('/<int:model_id>/edit', methods=['POST'])(update)
# mp.route('/<int:model_id>', methods=['DELETE'])(delete)
from flask import Blueprint
from controllers.UserController import login, signup, get_all_user

user = Blueprint('user',__name__)

user.route('/get-all',methods=["GET"])(get_all_user)
user.route('/login',methods=["POST"])(login)
user.route('/signup',methods=["POST"])(signup)



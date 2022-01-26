import jwt
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from flask import jsonify, request, make_response
from werkzeug.security import check_password_hash
from utils.JwtToken import token_required
from models.UserModel import UserModel as User
from models import db

load_dotenv()

# User Database Route
# this route sends back list of users users
@token_required
def get_all_user(current_user):
    
    output = User.get_all_users()
  
    return jsonify({'users': output})
  
# route for logging user in

def login():

    # creates dictionary of form data
    auth = request.form
  
    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = User.get_user_by_email(auth.get('email'))
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode(
            {
                'public_id': user.public_id,
                'exp' : datetime.utcnow() + timedelta(minutes = int(os.getenv('expiration_minutes')))
            }, 
            os.getenv("SECRET_KEY"),
            "HS256",
            )
        return make_response(jsonify({'token' : token}), 201)

    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )
  
# signup route
def signup():
    # creates a dictionary of the form data
    data = request.form.to_dict()

    response = User.create_user(data)
    
    return jsonify(response)
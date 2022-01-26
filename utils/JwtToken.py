import jwt
import os

from dotenv import load_dotenv
from functools import wraps
from flask import request, jsonify

from models.UserModel import UserModel as User

load_dotenv()

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        print(token)
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
        # decoding the payload to fetch the stored details
            data = jwt.decode(token, os.getenv('SECRET_KEY'),["HS256"])
            print(data)
            current_user = User.query\
                .filter_by(public_id = data['public_id'])\
                .first()
        except Exception as e:
            print(e)
            return jsonify({
                'message' : str(e)
            }), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated
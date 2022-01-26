from .Models import User
import uuid

class UserModel(User):

    @property
    def serialize(self):
        return {
            "name" : self.name,
            "last_name" : self.last_name,
            "email" : self.email
        }
    
    def get_all_users():
        # querying the database
        # for all the entries in it
        users = UserModel.get_all()

        return users
    
    def create_user(data):
        user = UserModel.get_user_by_email(data.get('email'))
        if not user:
            data["public_id"] = str(uuid.uuid4())
            new_user = UserModel.insert(data)
            
            return new_user
        else:
            # returns 202 if user already exists
            return {"message" : "User Already exists"}
        
    def get_user_by_email(email):

        # checking for existing user
        user = UserModel.query\
            .filter_by(email = email)\
            .first()
        return user
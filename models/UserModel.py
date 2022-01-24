from .Models import User

class UserModel(User):

    @property
    def serializer(self):
        return {
            "name" : self.name,
            "last_name" : self.last_name,
            "email" : self.email
        }
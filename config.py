import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

#Grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

#Enable debug mode
DEBUG = True

# Connect to the database 
#our database url
SQLALCHEMY_DATABASE_URI = os.getenv('uri')

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
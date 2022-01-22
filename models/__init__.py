from pymysql import install_as_MySQLdb
from flask_sqlalchemy import SQLAlchemy

install_as_MySQLdb()

db = SQLAlchemy()
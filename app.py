from flask import Flask
from flask_migrate import Migrate

from models import db

from routes.article_blueprint import article

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(article, url_prefix='/article')








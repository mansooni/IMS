from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

admin = Admin(app, template_mode='bootstrap3')

from app import views, forms, models


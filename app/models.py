from app import db 
from flask_login import UserMixin
from flask_admin.contrib.mongoengine import ModelView
from werkzeug.security import generate_password_hash


class User(UserMixin, db.Document):
    meta = {'collection':'userlist'}
    username = db.StringField(min_length=4, max_length=15)
    password = db.StringField(min_length=8, max_length=80)

class UserView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password, method='sha256')

from app import db
from flask_security import UserMixin, RoleMixin
from flask_admin.contrib.mongoengine import ModelView
from werkzeug.security import generate_password_hash
from flask import redirect, url_for
from flask_login import current_user

class Role(RoleMixin, db.Document):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(UserMixin, db.Document):
    username = db.StringField(min_length=4, max_length=15)
    password = db.StringField(min_length=8, max_length=80)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

class UserView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password, method='sha256')

    def is_accessible(self):
        return current_user.has_role('admin')

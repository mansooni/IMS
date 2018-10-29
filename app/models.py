from app import db
from flask_login import UserMixin


class User(UserMixin, db.Document):
    meta = {'collection':'userlist'}
    username = db.StringField(min_length=4, max_length=15)
    password = db.StringField(min_length=8, max_length=80)



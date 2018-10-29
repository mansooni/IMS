from  app import app, db, login_manager
from flask import render_template, request, redirect, url_for
from app.forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

@app.route('/', methods=['POST','GET'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        chk_usr = User.objects(username=form.username.data).first()
        if chk_usr:
            if User.objects(password=form.password.data).first():
                login_user(chk_usr)
                return redirect(url_for('success'))
    return render_template('index.html', form=form)


@app.route('/success')
@login_required
def success():
    return '<h1> Hello World!</h1>'

from  app import app, db, login_manager, admin
from flask import render_template, request, redirect, url_for
from app.forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from app.models import  User, UserView
from werkzeug.security import check_password_hash


admin.add_view(UserView(User))

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

@app.route('/', methods=['POST','GET'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        chk_usr = User.objects(username=form.username.data).first()
        if chk_usr:
            if check_password_hash(chk_usr['password'],form.password.data):
                login_user(chk_usr)
                if form.username.data == 'admin':
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/admin')
@login_required
def admin():
    return render_template('/admin/index.html')

@app.route('/success')
@login_required
def success():
    return '<h1> Hello World!</h1>'

from  app import app, db, login_manager, admin
from flask import render_template, request, redirect, url_for
from app.forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from app.models import  User, UserView, Role
from werkzeug.security import check_password_hash,generate_password_hash
from flask_security import Security, roles_required, MongoEngineUserDatastore

admin.add_view(UserView(User))

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

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
                if current_user.username == 'admin':
                    return redirect(url_for('admin.index'))
                else:
                    return redirect(url_for('success'))
                return redirect(url_for('login'))
    return render_template('index.html', form=form)

@app.route('/login')
@login_required
def login():
#    if current_user.get_role('admin'):
#        return "<h1>hello world</h1>"
#    else:
    return redirect(url_for('success'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/success')
@login_required
def success():
    return '<h1> Hello! {}</h1>'.format(current_user.username)

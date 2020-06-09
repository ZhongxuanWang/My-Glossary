from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from user import User

auth = Blueprint('auth', __name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users/users.db'
# # Remember, every time you make changes to the column (such as adding one col or removing one col, change the value),
# # you have to do the following: open terminal from pycharm, python3.7, from app import db, db.create_all() and exit.
# db = SQLAlchemy(app)
# db.create_all()


@auth.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')


@auth.route('/signup')
def signup():
    return render_template('auth/register.html')


# def user_loader(func):
#     @wraps(func)
#     def wrapper(user_id):
#         func()
#         return 'a'
#
#     return wrapper


# def login_required(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         pass
#     return wrapper


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

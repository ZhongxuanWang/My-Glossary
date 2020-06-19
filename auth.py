from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

from user import User

auth = Blueprint('auth', __name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users/users.db'
# # Remember, every time you make changes to the column (such as adding one col or removing one col, change the value),
# # you have to do the following: open terminal from pycharm, python3.7, from app import db, db.create_all() and exit.
# db = SQLAlchemy(app)
# db.create_all()


@auth.route('/login', methods=['GET'])
def login():
    print("Login")
    return render_template('auth/login.html')


@auth.route('/signup')
def signup():
    print("Signup in get")
    return render_template('auth/signup.html')


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
    return redirect(url_for('index'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        return 'Unable to add the user to database.'
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@auth.route('/account_set')
@login_required
def account_set():
    if request.method == 'GET':
        return render_template('setting.html')
    else:
        new_email = request.form['email']
        new_psw = request.form['psw']

        if new_psw == '' or new_email == '':
            return 'new password or email address was left blank'

        user = User.query.get_or_404(current_user.id)

        # Accessing through form in edit
        user.email = new_email
        user.psw = new_psw
        try:
            db.session.commit()
        except:
            return 'unable to commit the change to the server.'
        return redirect('/profile')


@auth.route('/cancel account')
@login_required
def cancel():
    from app import current_user
    if current_user is None:
        return redirect(url_for('index'))
    try:
        db.session.delete(current_user)
        db.session.commit()
    except:
        return 'unable to delete the user.'
    return render_template('index.html', base_msg='Your account has been canceled')

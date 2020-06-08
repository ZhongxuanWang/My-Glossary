from functools import wraps

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# from app import app

# config = {
#     "DEBUG": True,  # some Flask specific configs
#     "CACHE_TYPE": "simple",  # Flask-Caching related configs
#     "CACHE_DEFAULT_TIMEOUT": 300
# }
# app.config.from_mapping(config)
# cache = Cache(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users/users.db'
# # Remember, every time you make changes to the column (such as adding one col or removing one col, change the value),
# # you have to do the following: open terminal from pycharm, python3.7, from app import db, db.create_all() and exit.
# db = SQLAlchemy(app)
# db.create_all()


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/signup')
def signup():
    return render_template('auth/register.html')


def user_loader(func):
    @wraps(func)
    def wrapper(user_id):

        func()
        return 'a'

    return wrapper


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        pass
    return wrapper


@user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)
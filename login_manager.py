from functools import wraps

from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

from app import app

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)
cache = Cache(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users/users.db'
# Remember, every time you make changes to the column (such as adding one col or removing one col, change the value),
# you have to do the following: open terminal from pycharm, python3.7, from app import db, db.create_all() and exit.
db = SQLAlchemy(app)
db.create_all()


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


class User(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :param str password: encrypted password for the user

    """
    # Class attributes, could be inherited
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


@user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)
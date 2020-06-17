from functools import wraps

from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    #     new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # Class attributes, could be inherited
    id = db.Column(db.Integer, primary_key=True, unique=True)  # primaryfro keys are required by SQLAlchemy
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)

    words = db.Column(db.String)
    number_of_words = 0

    def __init__(self, email, name, password):
        self.email = email
        self.password = password
        self.name = name

    def is_active(self):
        """True, as all users are active."""
        return True

    # IF YOU ENCOUNTERED SOME ERRORS, READ THE DOCUMENT FIRST ! YOU MAY FIND THINGS USEFUL!
    def get_id(self):
        """Return the id to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def get_words(self):
        return self.word.split(',')

    def add_word(self, word):
        self.number_of_words += 1
        self.word += ',' + word

    def get_words_len(self):
        return self.number_of_words

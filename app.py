from flask import Flask, render_template
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

__author__ = 'Zhongxuan Wang'
__doc__ = 'iGlossary'

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users/users.db'
# Remember, every time you make changes to the column (such as adding one col or removing one col, change the value),
# you have to do the following: open terminal from pycharm, python3.7, from app import db, db.create_all() and exit.
db = SQLAlchemy(app)
db.create_all()

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}


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


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id)



@app.route('/', methods=['Get'])
def index():
    return render_template('index.html')



def read_file(filename):
    try:
        with open(filename) as f:
            return f.readline()
    except IOError:
        print("IO ERROR Raised. Reading file failed,")
        f = open(filename, "w")
        f.write('email@example.com')
        f.close()
        return 'content'


def write_file(filename, file_content):
    try:
        with open(filename, 'w') as f:
            f.write(file_content)
    except IOError:
        print("IO ERROR Raised. Writing file failed,")
    return ''


if __name__ == '__main__':
    app.run(debug=False)

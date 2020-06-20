import sys
import logging

logging.basicConfig(stream=sys.stderr)

# This PATH must be full path.
PATH_TO_APP_FOLDER = './My_Glossary/'

# This name is your python folder name located either in venv or in your system. Mine is python3.6
PYTHON_FOLDER_NAME = 'python3.6'

sys.path.insert(0, PATH_TO_APP_FOLDER + '')
sys.path.append(PATH_TO_APP_FOLDER + 'templates/')
sys.path.append(PATH_TO_APP_FOLDER + 'static/')
sys.path.append(PATH_TO_APP_FOLDER + 'users/')
# sys.path.append(PATH_TO_APP_FOLDER + 'venv/lib/' + PYTHON_FOLDER_NAME + '/site-packages/')
sys.path.append("/usr/local/lib/" + PYTHON_FOLDER_NAME + "/dist-packages/")


from app import app as application
from app import db, LoginManager

application.config['SECRET_KEY'] = 'wwzzxxsecretekeytodatabase'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users/users.db'
application.config['SERVER_NAME'] = 'mg.dlearninglab.com'

db.init_app(application)

# blueprint for auth routes in our app
from auth import auth as auth_blueprint
application.register_blueprint(auth_blueprint)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    print('in load user function')
    # print('User ID:', user_id)
    # since the user_id is just the primary key of our user table, use it in the query for the user
    from user import User
    return User.query.get(int(user_id))

# application.run(debug=True)

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
#
#
# # init SQLAlchemy so we can use it later in our models
# db = SQLAlchemy()
#
#
# def create_app():
#     appl = Flask(__name__)
#     login = LoginManager(appl)
#
#     appl.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
#     appl.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users/users.db'
#
#     db.init_app(appl)
#
#     # blueprint for auth routes in our app
#     from .auth import auth as auth_blueprint
#     appl.register_blueprint(auth_blueprint)
#
#     # blueprint for non-auth parts of app
#     from .app import app_blueprint as main_blueprint
#     appl.register_blueprint(main_blueprint)
#
#     return appl
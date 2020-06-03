from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import requests


__author__ = 'Zhongxuan Wang'
__doc__ = 'Never Forget online remainder'

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
# Remember, every time you make changes to the column (such as adding one col or removing one col, change the value),
# you have to do the following: open terminal from pycharm, python3.7, from app import db, db.create_all() and exit.
# db = SQLAlchemy(app)
# db.create_all()

datetime_format = '%b-%d-%Y %H:%M'

'''
This part requires your email information in order to receive email notifications. (This is left blank intentionally)
'''
email_account = ''
email_password = ''



if __name__ == '__main__':
    app.run(debug=False)

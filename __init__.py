from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///demo.db'
app.config['SECRET_KEY'] = '8a71aec88413c588fd73a58e'
db = SQLAlchemy(app) 
bcrypt = Bcrypt(app)
from market import routes


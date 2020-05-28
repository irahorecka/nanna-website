from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'a56a4d216cfdac7b852a76efd4fdc5e1'  # make this an environment variable at some point
db = SQLAlchemy(app)

from nannaElise import routes
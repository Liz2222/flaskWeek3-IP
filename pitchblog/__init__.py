from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import SECRET_KEY

app = Flask(__name__)


app.config['SECRET_KEY']='SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

from pitchblog import routes
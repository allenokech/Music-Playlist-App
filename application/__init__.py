from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@35.246.16.254/music_playlist_db"
app.config["SECRET_KEY"] = "jldhfgjlsdbn"
db = SQLAlchemy(app)

from application import routes
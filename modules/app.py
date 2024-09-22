import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from modules import db
from modules.models import User_mgmt, Post, Retweet, Timeline, Bookmark

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User_mgmt.query.get(int(user_id))

# For testing, use this code to create the database tables if they don't exist
with app.app_context():
    db.create_all()

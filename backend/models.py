from datetime import datetime
from backend import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    eth_address = db.Column(db.String(34) , unique=True , nullable=False)
    
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.bc_address}')"

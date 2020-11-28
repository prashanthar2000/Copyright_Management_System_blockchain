from backend import app , db ,  bcrypt
from flask import render_template, url_for, flash, redirect, request, abort
from backend.contract import contract #function to contract blockchain
from flask_login import login_user, current_user, logout_user, login_required
from backend.forms import  LoginForm
from backend.models import User


@app.route('/')
def home():
    return render_template('about.html')
    
# @app.route('/insertUser' , methods=["GET", "POST"] )
# def insertUser():



@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(eth_address=form.eth_address.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('event_index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route('/register' , methods=['GET' , "POST"])
def register():
    return render_template('main.html')



@app.route("/logout")
def logout():
    # logout_user()
    return redirect(url_for('home'))


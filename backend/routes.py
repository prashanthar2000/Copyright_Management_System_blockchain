from backend import app , db ,  bcrypt
from flask import render_template, url_for, flash, redirect, request, abort
# from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():
    return render_template('about.html')
    
# @app.route('/insertUser' , methods=["GET", "POST"] )
# def insertUser():



@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('main.html')
    



@app.route("/logout")
def logout():
    # logout_user()
    return redirect(url_for('home'))


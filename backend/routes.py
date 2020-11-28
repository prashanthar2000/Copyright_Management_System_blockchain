from backend import app , db ,  bcrypt
from flask import render_template, url_for, flash, redirect, request, abort
from backend.contract import contract #function to contract blockchain
from flask_login import login_user, current_user, logout_user, login_required
from backend.forms import  LoginForm , RegisterForm
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            if contract.function.insertUser(form.eth_address.data ,form.username, "owner" ).call():
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = User(username=form.username.data, eth_address=form.eth_address.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created! You are now able to log in', 'success')
                return redirect(url_for('login'))
        except:
            flash("Error occured while processing please try again " ,'danger')
            return render_template('main.html' , form=form)

    return render_template('main.html', title='Register', form=form)


@app.route("/createtoken" , methods=["GET" , "POST"])
@login_required
def createtoken():
    try:
        #not sure about this part i havent tested it yet
        contract.function.createtoken(current_user.eth_address).call()
        flash('Your token has been created!', 'success')
        return redirect(url_for('login'))

    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this


@app.route('/transfertokens', methods=["GET" , "POST"])
@login_required
def transfertokens():
    try:
        contract.function.transfertokens(current_user.eth_address, request.data['token']).call()
        flash("transaction successful" , 'success')
        return redirect(url_for('main.html'))
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 


@app.route('/getnumberoftokens')
def getnumberoftokens():
    try:
        return contract.function.getnumberoftokens().call()
        # flash("transaction successful" , 'success')
        # return redirect(url_for('main.html'))
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 


@app.route('/getUserCount')
def getUserCount():
    try:
        return contract.function.getUserCount().call()
    
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 




@app.route("/getnumberoftokenownedbyuser")
def getnumberoftokenownedbyuser():
    try:
        return contract.function.getnumberoftokenownedbyuser(request.args.get('eth_address')).call()
    
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 
    

@app.route("/getUserinfo")
def getUserinfo():
    try :
        return contract.functions.getUserinfo(request.args.get("eth_address")).call()
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 

@app.route("/gettokenowner")
def gettokenowner():
    try :
        return contract.functions.gettokenowner(request.args.get("id")).call()
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 

@app.route("/logout")
def logout():
    # logout_user()
    return redirect(url_for('home'))


from backend import app , db ,  bcrypt , contract
from flask import render_template, url_for, flash, redirect, request, abort
# from backend.contract import contract , w3 #function to contract blockchain
from flask_login import login_user, current_user, logout_user, login_required
from backend.forms import  LoginForm , RegisterForm
from backend.models import User 
from backend.contract import create_contract

from backend import contract


@app.route('/home')
def home():
    return render_template('about.html')
    
# @app.route('/insertUser' , methods=["GET", "POST"] )
# def insertUser():



@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(eth_address=form.eth_address.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main'))
        else:
            flash('Login Unsuccessful. Please check eth address and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route('/register' , methods=['GET' , "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            if contract.functions.insertUser(str(form.eth_address.data) ,str(form.username.data), "owner" ).transact():
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = User(username=form.username.data, eth_address=form.eth_address.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created! You are now able to log in', 'success')
                return redirect(url_for('login'))
        except Exception as e:
            print(e , type(e) )
            print(form.eth_address.data , form.username.data)
            flash("Error occured while processing please try again " ,'danger')
            return render_template('register.html' , form=form)

    return render_template('register.html', title='Register', form=form)


@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/createtoken" , methods=["GET" , "POST"])
@login_required
def createtoken():
    print(current_user)
    print(list(contract.functions))
    try:
        #not sure about this part i havent tested it yet
        contract.functions.createtoken(str(current_user.eth_address)).transact()
        flash('Your token has been created!', 'success')
        return render_template('main.html')

    except Exception as e:
        print(e , type(e) )
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this


@app.route('/transfertokens', methods=["GET" , "POST"])
@login_required
def transfertokens():
    print(current_user)
    print(type(request), request , request.args , request.data)
    try:
        contract.functions.transfertokens(str(current_user.eth_address), str(request.args['eth_address']), int(request.args['token'])).transact()
        flash("transaction successful" , 'success')
        return redirect(url_for('main.html'))
    except Exception as e:
        print(current_user.eth_address , request.args)
        print(e , type(e) )
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 


@app.route('/getnumberoftokens')
def getnumberoftokens():
    try:
        ret = contract.functions.getnumberoftokens().call()
        return str(ret)
        # flash("transaction successful" , 'success')
        # return redirect(url_for('main.html'))
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 


@app.route('/getUserCount')
def getUserCount():
    try:
        ret = contract.functions.getUserCount().call()
        return str(ret)
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 




@app.route("/getnumberoftokenownedbyuser")
def getnumberoftokenownedbyuser():
    try:
        ret= contract.functions.getnumberoftokenownedbyuser(request.args.get('eth_address')).call()
        return str(ret)
    except Exception as e:
        print(e , type(e))
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 
    

@app.route("/getUserinfo")
def getUserinfo():
    try :
        ret = contract.functions.getUserinfo(request.args.get("eth_address")).call()
        return str(ret)
    except:
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 

@app.route("/gettokenowner")
def gettokenowner():
    print(request.args)
    try :
        ret = contract.functions.gettokenowner(int(request.args.get("id"))).call()
        return str(ret)
    except Exception as e:
        print(e , type(e))
        flash("Error occured while processing please try again " ,'danger')
        return render_template('main.html')#change this 

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,  TextAreaField ,DateField , BooleanField
from wtforms.validators import DataRequired, Optional #, Length, Email, EqualTo, ValidationError
from wtforms import validators
from backend.models import User

# import re
address_pat = r"0x[0-9a-fA-F]+"


class LoginForm(FlaskForm):
    # email = StringField('Email',validators=[DataRequired(), Email()])
    eth_address = StringField('eth_address',[
        validators.Regexp(address_pat, message="eth address must contain hex-decimal digits as input only")])
    
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    eth_address = StringField('eth_address' ,[validators.Regexp(address_pat, message="eth address must contain hex-decimal digits as input only")])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('Username' , validators=[DataRequired()]) 
       
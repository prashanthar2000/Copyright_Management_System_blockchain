from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField , TextAreaField ,DateField
from wtforms.validators import DataRequired, Optional #, Length, Email, EqualTo, ValidationError

import re

address_pat = r"0x[0-9a-fA-]{32}"


from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from wtforms import ValidationError

from flask_login import current_user
from Blogwebsite.models import Users

class Registration_form(FlaskForm):
	username=StringField('Username',validators=[DataRequired()])
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired(),EqualTo('Confirm_Password',message="Passwords must match!!")])
	Confirm_Password=PasswordField('Confirm_Password',validators=[DataRequired()])
	Submit=SubmitField('Register!')

	def Validate_email(self,field):
		if Users.query.filterby(email=field.data).first():
			raise ValidationError('Your email has been registered already!')
	def Validate_username(self,field):
		if Users.query.filterby(Username=field.data).first():
			raise ValidationError('Username already exists')

class Login_form(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	Submit = SubmitField('Login!')




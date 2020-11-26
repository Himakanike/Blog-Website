from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,TextAreaField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from wtforms import ValidationError

class contact_form(FlaskForm):
	Name=StringField('Name',validators=[DataRequired(), Length(min=1,max=30)])
	Email=StringField('Email',validators=[DataRequired(), Email(), Length(min=1,max=30)])
	Subject=StringField('Subject',validators=[DataRequired(), Length(min=1,max=30)])
	Message= TextAreaField('Message',validators=[DataRequired(), Length(min=1,max=200)])
	Submit=SubmitField('Submit')
'''class login_form(FlaskForm):
	Username=StringField('Username',validators=[DataRequired(), Length(min=1,max=30)])
	Password=PasswordField('Password',validators=[DataRequired(),EqualTo('Confirm', message='Passwords must match')])
	Confirm=PasswordField('Repeat Password')
	Submit=SubmitField('Submit')
EqualTo('Confirm', message='Passwords must match')'''
class Addpost_form(FlaskForm):
	Title=StringField('Title',validators=[DataRequired(), Length(min=1,max=30)])
	Content=TextAreaField('Content',validators=[DataRequired(), Length(min=1,max=3000)])
	Submit=SubmitField('Submit')

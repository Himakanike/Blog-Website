from Blogwebsite import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
'''MODELS'''
class Contact_info(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	Name=db.Column(db.String(20))
	Email=db.Column(db.String(30),unique=True)
	Subject=db.Column(db.String(20))
	Message=db.Column(db.String(300))
	def __init__(self,Name,Email,Subject,Message):
		self.Name=Name
		self.Email=Email
		self.Subject=Subject
		self.Message=Message
	def __repr__(self):
		return f"Contact Id: {self.Id} --- Name: {self.Name} --- Email: {self.Email} --- Subject: {self.Subject} --- Message: {self.Message}"
class Postss(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	Title=db.Column(db.String(200))
	Content=db.Column(db.String(300))
	def __init__(self,Title,Content):
		self.Title=Title
		self.Content=Content
	def __repr__(self):
		return f"Posts Id: {self.Id} --- Title: {self.Title} --- Content: {self.Content}"

class Users(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	email=db.Column(db.String(20))
	username=db.Column(db.String(20))
	Password_hash=db.Column(db.String(20))
	def __init__(self,email,username,Password):
		self.email=email
		self.username=username
		self.Password_hash=generate_password_hash(Password)
	def check_password(self,password):
		# https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
		return check_password_hash(self.Password_hash,password)


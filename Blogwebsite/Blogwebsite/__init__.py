import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
'''db.create_all()'''
Migrate(app,db)

###########################
#### BLUEPRINT CONFIGS #######
#########################
login_manager = LoginManager()

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "users.login"

# Import these at the top if you want
# We've imported them here for easy reference
from Blogwebsite.core.views import core
from Blogwebsite.Posts.views import Posts
from Blogwebsite.User.views import User


# Register the apps
app.register_blueprint(core)
app.register_blueprint(Posts)
app.register_blueprint(User)



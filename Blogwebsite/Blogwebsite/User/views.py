from flask import render_template,redirect,url_for,Blueprint,flash,request
from Blogwebsite.User.forms import Registration_form,Login_form
from Blogwebsite.models import Users
from flask_login import login_user,logout_user,current_user,login_required
from Blogwebsite import db
from werkzeug.security import generate_password_hash,check_password_hash


User = Blueprint('User', __name__)

@User.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration_form()

    if form.validate_on_submit():
        user = Users(email=form.email.data,
                    username=form.username.data,
                    Password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('User.Login'))
    return render_template('Register.html', form=form)

@User.route('/Login', methods=['GET', 'POST'])
def Login():

    form = Login_form()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = Users.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user
            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            '''next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('core.Home')'''

            return redirect(url_for('Posts.Functions'))
    return render_template('Login.html', form=form)


@User.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('core.Home'))




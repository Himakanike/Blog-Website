from flask import render_template,request,Blueprint
from Blogwebsite.models import Postss,Contact_info
from Blogwebsite.Posts.Form import contact_form,Addpost_form 
from flask import url_for,flash, redirect,Blueprint
from Blogwebsite import db
'''from Blogwebsite.Posts.Form import contact_form,Addpost_form'''
core = Blueprint('core',__name__)

'''@core.route('/')
def Home():
	Blogposts=Posts.query.all()
	return render_template('Home.html',Blogposts=Blogposts)'''
		


@core.route('/')
def Home():
	PostsList=Postss.query.all()
	return render_template('Home.html',PostsList=PostsList)

@core.route('/About')
def About():
	return render_template('About.html')

@core.route('/Admin')
def Admin():
	return render_template('Admin.html')


'''@core.route('/Contact',methods=['GET','POST'])
def Contact():
	f=contact_form()
	if f.validate_on_submit():
		record=Contact_info(Name=f.Name.data,Email=f.Email.data,
			                  Subject=f.Subject.data,Message=f.Message.data)
		db.session.add(record)
		db.session.commit()
		flash("so done")
		return redirect(url_for('core.Contact_list'))
	return render_template('Contact.html',f=f)

@core.route('/Contact_list',methods=['GET','POST'])
def Contact_list():
	Contacts=Contact_info.query.all()
	return render_template('Contact_list.html',Contacts=Contacts)

@core.route('/Add_Post',methods=['GET','POST'])
def Add_Post():
	f=Addpost_form()
	if f.validate_on_submit():
		record=Posts(Title=f.Title.data,Content=f.Content.data)
		db.session.add(record)
		db.session.commit()
		flash("So donneeeee")
		return redirect(url_for('core.Home'))
	return render_template('Add_Post.html',f=f)'''



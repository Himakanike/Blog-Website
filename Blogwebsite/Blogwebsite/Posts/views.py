from flask import render_template,url_for,flash, redirect,request,Blueprint
from Blogwebsite import db
from flask_login import current_user,login_required
from Blogwebsite.models import Contact_info,Postss
from Blogwebsite.Posts.Form import contact_form,Addpost_form
from flask import request

Posts = Blueprint('Posts',__name__)

@Posts.route('/Add_Post',methods=['GET','POST'])
def Add_Post():
	f=Addpost_form()
	if f.validate_on_submit():
		record=Postss(Title=f.Title.data,Content=f.Content.data)
		db.session.add(record)
		db.session.commit()
		'''return redirect(url_for('core.Home'))'''
		flash("So donneeeee")
		return redirect(url_for('core.Home'))
	return render_template('Add_Post.html',f=f)

@Posts.route("/<int:post_id>/delete",methods=['GET','POST'])
def delete(post_id):
	blog_post = Postss.query.get_or_404(post_id)
	db.session.delete(blog_post)
	db.session.commit()
	flash('Post has been deleted')
	return redirect(url_for('core.Home'))


@Posts.route('/Contact',methods=['GET','POST'])
def Contact():
	f=contact_form()
	if f.validate_on_submit():
		record=Contact_info(Name=f.Name.data,Email=f.Email.data,
							  Subject=f.Subject.data,Message=f.Message.data)
		db.session.add(record)
		db.session.commit()
		flash("so done")
		return redirect(url_for('Posts.Contact_list'))
	return render_template('Contact.html',f=f)

@Posts.route('/Contact_list',methods=['GET','POST'])
def Contact_list():
	Contacts=Contact_info.query.all()
	return render_template('Contact_list.html',Contacts=Contacts)

@Posts.route('/Functions',methods=['GET','POST'])
@login_required
def Functions():
	return render_template('Functions.html')
	



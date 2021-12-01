from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO
from Misc.functions import *

from Controllers.AdminManager import AdminManager
from Controllers.BookManager import BookManager

admin_view = Blueprint('admin_routes', __name__, template_folder='../templates/admin/', url_prefix='/admin')

book_manager = BookManager(DAO)
admin_manager = AdminManager(DAO)


@admin_view.route('/', methods=['GET'])
@admin_manager.admin.login_required
def home():
	admin_manager.admin.set_session(session, g)

	return render_template('admin/home.html', g=g)


@admin_view.route('/signin/', methods=['GET', 'POST'])
@admin_manager.admin.redirect_if_login
def signin():
	g.bg = 1
	
	if request.method == 'POST':
		_form = request.form
		email = str(_form["email"])
		password = str(_form["password"])

		if len(email)<1 or len(password)<1:
			return render_template('admin/signin.html', error="Email and password are required")

		d = admin_manager.signin(email, hash(password))

		if d and len(d)>0:
			session['admin'] = int(d["id"])

			return redirect("/admin")

		return render_template('admin/signin.html', error="Email or password incorrect")

	return render_template('admin/signin.html')


@admin_view.route('/signout/', methods=['GET'])
@admin_manager.admin.login_required
def signout():
	admin_manager.signout()

	return redirect("/admin/", code=302)


@admin_view.route('/users/view/', methods=['GET'])
@admin_manager.admin.login_required
def users_view():
	admin_manager.admin.set_session(session, g)

	id = int(admin_manager.admin.uid())
	admin = admin_manager.get(id)
	myusers = admin_manager.getUsersList()

	return render_template('users.html', g=g, admin=admin, users=myusers)



@admin_view.route('/books/', methods=['GET'])
@admin_manager.admin.login_required
def books():
	admin_manager.admin.set_session(session, g)

	print('----------------------------------')
	print(admin_manager.admin.uid())
	print('----------------------------------')
	id = int(admin_manager.admin.uid())
	admin = admin_manager.get(id)
	mybooks = book_manager.list()

	return render_template('books/views.html', g=g, books=mybooks, admin=admin)


@admin_view.route('/books/add', methods=['GET', 'POST'])
@admin_manager.admin.login_required
def book_add():
	return render_template('books/add.html', g=g)


@admin_view.route('/books/edit', methods=['GET', 'PUT'])
@admin_manager.admin.login_required
def book_edit():
	return render_template('books/edit.html', g=g)

@admin_view.route('/books/delete/<id>', methods=['GET'])
@admin_manager.admin.login_required
def book_delete(id):
	id = int(id)

	if id is not None:
		book_manager.delete(id)
	
	return redirect('/admin/books/')
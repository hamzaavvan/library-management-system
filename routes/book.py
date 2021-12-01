from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response
from app import DAO

from Controllers.UserManager import UserManager
from Controllers.BookManager import BookManager

book_view = Blueprint('book_routes', __name__, template_folder='/templates')

book_manager = BookManager(DAO)
user_manager = UserManager(DAO)

@book_view.route('/books/', defaults={'id': None})
@book_view.route('/books/<int:id>')
def home(id):
	user_manager.user.set_session(session, g)

	if id != None:
		b = book_manager.getBook(id)

		print('----------------------------')
		print(b)
		
		if b and len(b) <1:
			return render_template('book_view.html', error="No book found!")

		return render_template("book_view.html", books=b, g=g)
	else:
		b = book_manager.list()
		
		if b and len(b) <1:
			return render_template('books.html', error="No books found!")
	
		return render_template("books.html", books=b, g=g)


	return render_template("books.html", books=b, g=g)


@book_view.route('/books/add/<id>', methods=['GET'])
@user_manager.user.login_required
def add(id):
	user_id = user_manager.user.uid()
	book_manager.reserve(user_id, id)

	b = book_manager.list()
	user_manager.user.set_session(session, g)
	
	return render_template("books.html", msg="Book reserved", books=b, g=g)


@book_view.route('/books/search', methods=['GET'])
def search():
	user_manager.user.set_session(session, g)

	if "keyword" not in request.args:
		return render_template("search.html")

	keyword = request.args["keyword"]

	if len(keyword)<1:
		return redirect('/books')

	d=book_manager.search(keyword)

	if len(d) >0:
		return render_template("books.html", search=True, books=d, count=len(d), keyword=escape(keyword), g=g)

	return render_template('books.html', error="No books found!", keyword=escape(keyword))


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

	user_books = []
	if user_manager.user.isLoggedIn():
		reserved_books = book_manager.getReserverdBooksByUser(user_id=user_manager.user.uid())
		user_books = reserved_books.get('user_books', '').split(',') if reserved_books else []

	if id is not None:
		b = book_manager.getBook(id)
		template = 'book_view.html'
	else:
		b = book_manager.list()
		template = 'books.html'

	if not b:
		return render_template(template, error="No book(s) found!")

	return render_template(template, books=b, g=g, user_books=user_books)

@book_view.route('/books/me')
@user_manager.user.login_required
def mybooks():
	user_manager.user.set_session(session, g)

	user_books = []
	reserved_books = book_manager.getReserverdBooksByUser(user_id=user_manager.user.uid())
	user_books = reserved_books.get('user_books', '').split(',') if reserved_books else []
	b = book_manager.getUserBooks(user_manager.user.uid())

	if not b:
		return render_template('books.html', error="No book(s) found!", view='mybooks')

	return render_template('books.html', books=b, g=g, user_books=user_books, count=len(user_books), view='mybooks')

@book_view.route('/books/add/<id>', methods=['GET'])
@user_manager.user.login_required
def add(id):
	user_id = user_manager.user.uid()

	reserved_books = book_manager.getReserverdBooksByUser(user_id=user_manager.user.uid())
	reserved_books = reserved_books.get('user_books', '').split(',') if reserved_books else []
	
	b = book_manager.list()
	if id in reserved_books:
		return render_template("books.html", error="Book already reserved", books=b, g=g, user_books=reserved_books)
		
	book_manager.reserve(user_id, id)
	user_manager.user.set_session(session, g)
	
	return render_template("books.html", msg="Book reserved", books=b, g=g, user_books=reserved_books)


@book_view.route('/books/search', methods=['GET'])
def search():
	user_manager.user.set_session(session, g)
	
	reserved_books = book_manager.getReserverdBooksByUser(user_id=user_manager.user.uid())
	reserved_books = reserved_books.get('user_books', '').split(',') if reserved_books else []

	if "keyword" not in request.args:
		return render_template("search.html")

	keyword = request.args["keyword"]

	if len(keyword)<1:
		return redirect('/books')

	d=book_manager.search(keyword)

	if len(d) >0:
		return render_template("books.html", search=True, books=d, count=len(d), keyword=escape(keyword), g=g, user_books=reserved_books)

	return render_template('books.html', error="No books found!", keyword=escape(keyword), user_books=reserved_books)


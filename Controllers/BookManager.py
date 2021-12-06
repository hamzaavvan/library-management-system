from App.Books import Books

class BookManager():
	def __init__(self, DAO):
		self.misc = Books(DAO.db.book)
		self.dao = self.misc.dao

	def list(self, availability=1):
		book_list = self.dao.list(availability)

		return book_list

	def getBook(self, id):
		books = self.dao.getBook(id)

		return books

	def search(self, keyword, availability=1):
		books = self.dao.search_book(keyword, availability)

		return books

	def reserve(self, user_id, book_id):
		books = self.dao.reserve(user_id, book_id)

		return books

	def getUserBooks(self, user_id):
		books = self.dao.getBooksByUser(user_id)

		return books

	def delete(self, id):
		self.dao.delete(id)
from App.User import User

class UserManager():
	def __init__(self, DAO):
		self.user = User(DAO.db.user)
		self.book = DAO.db.book
		self.dao = self.user.dao

	def list(self):
		user_list = self.dao.list()

		return user_list

	def signin(self, email, password):
		user = self.dao.getByEmail(email)

		if user is None:
			return False

		user_pass = user['password'] # user pass at 
		if user_pass != password:
			return False

		return user

	def signout(self):
		self.user.signout()
		
	def get(self, id):
		user = self.dao.getById(id)

		return user

	def signup(self, name, email, password):
		user = self.dao.getByEmail(email)

		if user is not None:
			return "already_exists"

		user_info = {"name": name, "email": email, "password": password}
		
		new_user = self.dao.add(user_info)

		return new_user
		
	def get(self, id):
		user = self.dao.getById(id)

		return user
		
	def update(self, name, email, password, bio, id):
		user_info = {"name": name, "email": email, "password": password, "bio":bio}
		
		user = self.dao.update(user_info, id)

		return user

	def getBooksList(self, id):
		return self.book.getBooksByUser(id)

	def getUsersByBook(self, book_id):
		return self.dao.getUsersByBook(book_id)
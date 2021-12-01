from copy import copy

from Models.BookDAO import BookDAO
from Models.UserDAO import UserDAO
from Models.AdminDAO import AdminDAO

from Models.DB import DB

class DBDAO(DB):
	def __init__(self, app):
		super(DBDAO, self).__init__(app)

		self.book = BookDAO(copy(self))
		self.user = UserDAO(copy(self))
		self.admin = AdminDAO(copy(self))

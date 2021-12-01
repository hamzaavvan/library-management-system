from Models.DBDAO import DBDAO

class DAO():
	def __init__(self, app):
		self.db = DBDAO(app)
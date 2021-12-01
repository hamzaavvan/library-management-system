from App.Actor import Actor

class User(Actor):
	id = 0
	name = ""
	lock = False

	user = {}

	def __init__(self, UserDAO):
		self.dao = UserDAO
		self.sess_key = "user" # session key
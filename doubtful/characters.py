class Player(object):
	def __init__(self):
		self.name = ''
		self.room = ''
	def move(self, direction):
		print self.room.paths()

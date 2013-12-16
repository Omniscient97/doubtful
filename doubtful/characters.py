BLACKLIST_NAMES = ['jim']

class Player(object):
	def __init__(self):
		self.name = ''
		self.room = ''
	def set_name(self):
		while self.name == '':
			name = input('Please input your name: ').lower()
			if name not in BLACKLIST_NAMES:
				self.name = name.capitalize()


	def move(self, direction):
		print(self.room.exits())

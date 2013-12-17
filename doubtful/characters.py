BLACKLIST_NAMES = ['jim']


class Player(object):
	def __init__(self):
		self.name = ''
		self.room = ''
		self.type = 'player'
	def set_name(self):
		while self.name == '':
			name = input('Please input your name: ').lower()
			if name not in BLACKLIST_NAMES:
				self.name = name.capitalize()
	def talk(self, target):
		print("I will talk with %s soon." % target.name)


	def move(self, direction):
		print(self.room.exits())

class NPC(object):
	def __init__(self, name, room):
		self.name = name
		self.room = room
		self.type = 'person'
	def __str__(self):
		return self.name + '%s' % self.room.name + self.type
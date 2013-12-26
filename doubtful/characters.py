BLACKLIST_NAMES = ['jim']


class Player(object):
	def __init__(self):
		self.name = ''
		self.room = ''
		self.type = 'player'
	def set_name(self, player_input=False):
		if player_input != False:
			try:
				player_input = player_input.lower()
				player_input = player_input.capitalize()
				if player_input == '':
					raise AttributeError('Empty String')
				self.name = player_input
			except AttributeError:
				print('ERROR: Invalid-Name => Defaulting Player name to "Default"')
				self.name = 'Default'
		else:
			while self.name == '':
				name = input('Please input your name: ').lower()
				if name not in BLACKLIST_NAMES:
					self.name = name.capitalize()
	def talk(self, target):
		print('%s: ' % target.name + target.dialogue)

	def move(self, direction):
		if self.room.exits[direction] != 'none':
			self.room.inventory.remove(self)
			self.room.exits[direction].inventory.add(self)
			self.room = self.room.exits[direction]

class NPC(object):
	def __init__(self, name, room):
		self.name = name
		self.room = room
		self.type = 'person'
		self.dialogue = ''


	def __str__(self):
		return self.name + '%s' % self.room.name + self.type
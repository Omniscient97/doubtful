from lexicon import *

class Player(object):
	def __init__(self):
		self.name = ''

lexicon = Lexicon()
player = Player()

player.name = input('Please input your name: ')
print("hello,", player.name)
user_input = input('enter commands: ')
print(lexicon.scan(user_input))
input('press enter to exit ;)')

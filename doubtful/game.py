from lexicon import *
from room import *
from characters import *
from story import *
from room import *


def print_status(player):
	print('')
	print('Current Status for %s' % player.name)
	print('Room: %s' % player.room.name)
	print('Exits: %s' % 'Not Implemented Yet')
	print('')
lexicon = Lexicon()
player = Player()
player.set_name()
#player.name = input('Please input your name: ').capitalize()
print('Hello,', player.name)
print('Type "exit" to quit the game')

room1 = Room("Room 1", [])
room2 = Room("Room 2", [])
room3 = Room("Room 3", [])

player.room = room1

print_status(player)

game = True
while game:
	user_input = lexicon.scan(input('enter commands: '))
	for word in user_input:
		if word[1] == 'status':
			print('Coming soon.')
		if word[1] == "go":
			print('"go" is Coming soon.')
		if word[1] == 'exit':
			game = False
		if word[0] == 'error':
			print('I dont understand "%s"' % word[1])
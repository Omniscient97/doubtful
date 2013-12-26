from lexicon import *
from room import *
from characters import *
from story import *
from room import *
from item import *
from map import *
from config import *

def print_status(player):
	print('')
	print('Current Status for: %s' % player.name)
	print('Room: %s' % player.room.name)
	print('')
lexicon = Lexicon()
config = ConfigurationLoader('3')
config.load('doubtful/example.config')

player = Player()
player.set_name()
#player.name = input('Please input your name: ').capitalize()
print('Hello,', player.name)
print('Type "exit" to quit the game')



room1 = Room('Room 1','You\'re in a room which is completely empty save for the man standing beside you. There is a doorway to the North.', [])

jim = NPC('Jim', room1)
jim.dialogue = 'Who\'s that? Where are you? I can\'t see without my glasses! Have you seen them anywhere?'
jim_glasses = Item('Jim\'s Glasses')
room1.inventory.add(jim)
room1.inventory.add(player)
room2 = Room('Room 2','', [])
room2.inventory.add(jim_glasses)
room3 = Room('Room 3','', [])
room1.exits[2] = room2
room2.exits[0] = room1

player.room = room1
print('')
print(player.room.description)

game = True
while game:
	user_input = lexicon.parse(input('enter commands: '))
	for word in user_input:
		if word[1] == 'look':
			print(player.room.description)
			print(player.room.inventory.list_of_items_by_name())
		if word[1] == 'status':
			print_status(player)
		if word[1] == "go":
			player.move(2)
			print(player.room.description)
		if word[1] == 'help':
			print('available commands: %s' % 'PSYCHE')
			print("Verbs: %s" % return_verbs())
		if word[1] == 'talk':
			for item in player.room.inventory.list_of_items():
				if item.type == 'person':
					player.talk(item)
		if word[1] == 'map':
			print('Not implemented yet.')
		if word[1] == 'exit':
			game = False
		if word[0] == 'error':
			print('I dont understand "%s"' % word[1])
from lexicon import *
from room import *
from characters import *
from story import *

lexicon = Lexicon()
player = Player()

player.name = input('Please input your name: ')
print("hello,", player.name)
print('Type "exit" to quit the game')
game = True
while game:
	user_input = lexicon.scan(input('enter commands: '))
	for word in user_input:
		if word[1] == "exit":
			game = False
		if word[0] == "error":
			print('I dont understand "%s"' % word[1])
from nose.tools import *
from doubtful.config import *

def config_room_test():
	#setup_config('2')
	config = ConfigurationLoader('2')
	config.load('doubtful/example.config')
	rooms = config.sections()
	for room in rooms:
		#print config.options(room)
		pass

	#print config.getlist('Room1', 'exits')
	#print config.getlist('Room2', 'contents')
from nose.tools import *
from doubtful.room import *

def room_basic_test():
	room1 = Room('Treasure Room', 'A beautiful room filled with Gold coins and trinkets.', [])

	assert_equal(room1.name, 'Treasure Room')
	assert_equal(room1.description, 'A beautiful room filled with Gold coins and trinkets.')
	assert_equal(room1.exits, ['none', 'none', 'none', 'none'])
	assert_equal(room1.inventory.list_of_items(), [])
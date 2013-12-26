from nose.tools import *
from nose.tools import assert_raises
from doubtful.characters import *
from doubtful.room import Room

def player_basic_test():

	# Test room
	test_room = Room('Test Room', 'Money is raining from teh sky.', [])

	#### Name Testing

	# Test basic name setting
	test_player1 = Player()

	test_player1.set_name('josh')
	assert_equal(test_player1.name, 'Josh')
	test_player1.set_name('JOSH')
	assert_equal(test_player1.name, 'Josh')
	test_player1.set_name('lIAM')
	assert_equal(test_player1.name, 'Liam')

	# Test exception handling
	test_player2 = Player()
	test_player2.set_name(True)
	assert_equal(test_player2.name, 'Default')
	assert_raises(AttributeError, test_player2.set_name(55))
	assert_equal(test_player2.name, 'Default')
	assert_raises(AttributeError, test_player2.set_name(True))
	assert_equal(test_player2.name, 'Default')
	assert_raises(AttributeError, test_player2.set_name(''))
	assert_equal(test_player2.name, 'Default')
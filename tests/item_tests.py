from nose.tools import *
from doubtful.item import *

def item_basic_test():
	item1 = Item('Firesword')
	item2 = Item('Icepick')
	item3 = Item('Aegis of Light')

	assert_equal((item1.name, item1.type), ('Firesword', 'item'))
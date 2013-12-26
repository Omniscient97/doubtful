from nose.tools import *
from doubtful.inventory import *
from doubtful.item import Item

def inventory_basic_test():

	item1 = Item('Magic Carpet')
	item2 = Item('Newt')
	item3 = Item('Pistol')

	bag1 = Inventory()

	assert_equal(bag1.list_of_items(), [])
	bag1.add(item1)
	bag1.add(item2)
	bag1.add(item3)
	assert_equal(bag1.list_of_items(), [item1, item2, item3])
	assert_equal(bag1.list_of_items_by_name(), ['Magic Carpet', 'Newt', 'Pistol'])
	bag1.remove(item2)
	assert_equal(bag1.list_of_items(), [item1, item3])
	assert_equal(bag1.list_of_items_by_type('item'), ['Magic Carpet', 'Pistol'])
	assert_equal(bag1.list_of_items_by_type('room'), [])
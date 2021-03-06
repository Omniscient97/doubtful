from inventory import *

class Room(object):
	def __init__(self, name, description, contents):
		self.name = name
		self.description = description
		self.inventory = Inventory()
		for item in contents:
			self.inventory.add(item)
		self.exits = ['none', 'none', 'none', 'none'] # exits = [north, east, south, west]

	def add(self, item):
		self.inventory.add(item)
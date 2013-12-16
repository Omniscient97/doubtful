from inventory import *

class Room(object):
	def __init__(self, name, description, contents):
		self.name = name
		self.description = description
		self.inventory = Inventory()
		for item in contents:
			self.inventory.add(item)
		self.exits = [] # exits = [north, east, south, west]
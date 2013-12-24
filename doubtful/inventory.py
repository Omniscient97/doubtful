class Inventory(object):
	def __init__(self):
		self.contents = []
	def add(self, item):
		self.contents.append(item)
	def remove(self, item):
		self.contents.remove(item)
	def list_of_items(self, item_type='all', return_type='object'):
		return_list = []
		for item in self.contents:
			return_list.append(item)
		return return_list
	def list_of_items_by_name(self):
		return_list = []
		for item in self.contents:
			return_list.append(item.name)
		return return_list
	def list_of_items_by_type(self, item_type):
		return_list = []
		for item in self.contents:
			if item.type == item_type:
				return_list.append(item.name)
		return return_list
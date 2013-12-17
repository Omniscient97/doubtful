class Inventory(object):
	def __init__(self):
		self.contents = []
	def add(self, object):
		self.contents.append(object)
	def remove(self, object):
		self.contents.remove(object)
	def list_of_items(self):
		return_list = []
		for item in self.contents:
			return_list.append(item)
		return return_list
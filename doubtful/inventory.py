class Inventory(object):
	def __init__(self):
		self.contents = []
	def add(self, object):
		self.contents.append(object)
	def remove(self, object):
		self.contents.remove(object)
				
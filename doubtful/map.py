# Game Map:
#
#
#    000000000111111
#    123456789012345
#1   ===============
#2  | ----          |
#3  || @1 |         |
#4  ||#1,2|         |
#5  | -||-          |
#6  || @2 |         |
#7  ||#3  |         |
#8  | ----          |
#9  |               |
#10 |               |
#11 |               |
#12 |               |
#    ===============

#  @1 - Room 1
#  @2 - Room 2
#
#  #1 = You
#  #2 = Jim
#  #3 = Jim's Glasses

def print_map():
	print('     000000000111111\n     123456789012345\n1   ===============\n2  | ----          |\n3  || @1 |         |\n4  ||#1,2|         |\n5  | -||-          |\n6  || @2 |         |\n7  ||#3  |         |\n8  | ----          |\n9  |               |\n10 |               |\n11 |               |\n12 |               |\n    ===============\n')
	print('  @1 - Room 1\n  @2 - Room 2\n\n  #1 = You\n  #2 = Jim\n  #3 = Jim\'s Glasses')


class Map(object):
	def __init__(self):
		self.rooms = []
	def load_from_file(self, file):
		pass
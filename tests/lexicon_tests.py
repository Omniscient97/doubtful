from nose.tools import *
from doubtful.lexicon import Lexicon

def scan_test():
	lexicon = Lexicon()
	assert_equal(lexicon.scan('use key on door'), [('verb', 'use'), ('noun', 'key'), ('preposition', 'on'), ('noun', 'door')])
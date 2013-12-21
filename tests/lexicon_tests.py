from nose.tools import *
import doubtful.lexicon

def scan_test():
	lexicon = doubtful.lexicon.Lexicon()
	assert(lexicon.scan('use key on door'), [('verb', 'use'), ('noun', 'key'), ('preposition', 'on'), ('noun', 'door')])
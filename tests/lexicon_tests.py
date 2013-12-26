from nose.tools import *
from doubtful.lexicon import Lexicon

def lexicon_parse_test():
	lexicon = Lexicon()

	# Basic tokenising 
	assert_equal(lexicon.parse('use key on door'), [('verb', 'use'), ('noun', 'key'), ('preposition', 'on'), ('noun', 'door')])
	assert_equal(lexicon.parse('pick up glasses from table'), [('verb', 'pick'), ('direction', 'up'), ('noun', 'glasses'), ('preposition', 'from'), ('noun', 'table')])

	# Article stripping
	assert_equal(lexicon.parse('eat an apple'), [('verb', 'eat'), ('noun', 'apple')])
	assert_equal(lexicon.parse('listen to a song'), [('verb', 'listen'), ('preposition', 'to'), ('noun', 'song')])

	# Test Caps and Errors
	assert_equal(lexicon.parse('MAP'), [('command', 'map')])
	assert_equal(lexicon.parse('tHis IS CrAZy'), [('error', 'this'), ('error', 'is'), ('error', 'crazy')])

	# Jim's Scenario tests
	assert_equal(lexicon.parse('go south'), [('verb', 'go'), ('direction', 'south') ])
	assert_equal(lexicon.parse('look'), [('verb', 'look')])
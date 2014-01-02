from nose.tools import *
from doubtful.lexicon import Lexicon

def lexical_tokenise_test():
	lexicon = Lexicon()

	# Basic tokenising 
	assert_equal(lexicon.tokenise('use key on door'), [('verb', 'use'), ('noun', 'key'), ('preposition', 'on'), ('noun', 'door')])
	assert_equal(lexicon.tokenise('pick up glasses from table'), [('verb', 'pick'), ('direction', 'up'), ('noun', 'glasses'), ('preposition', 'from'), ('noun', 'table')])

	# Article stripping
	assert_equal(lexicon.tokenise('eat an apple'), [('verb', 'eat'), ('noun', 'apple')])
	assert_equal(lexicon.tokenise('listen to a song'), [('verb', 'listen'), ('preposition', 'to'), ('noun', 'song')])

	# Test Caps and Errors
	assert_equal(lexicon.tokenise('MAP'), [('command', 'map')])
	assert_equal(lexicon.tokenise('tHis IS CrAZy'), [('error', 'this'), ('error', 'is'), ('error', 'crazy')])

	# Jim's Scenario tests
	assert_equal(lexicon.tokenise('go south'), [('verb', 'go'), ('direction', 'south') ])
	assert_equal(lexicon.tokenise('look'), [('verb', 'look')])

def classify_test():

	# a Command object with a Verb containing its object which is class and contains modifiers
	#	Command
	#	 ^- verb = Verb
	#       ^- direct object, indirect_object (if applicable)
	#           ^- modifiers

	lexicon = Lexicon()

	# test verb/object with 1 adjective
	command = lexicon.classify([('verb', 'take'), ('adjective', 'red'), ('noun', 'key')])
	assert_equal(command.verb.name, 'take')
	assert_equal(command.object.name, 'key')
	assert_equal(command.object.modifiers, ['red'])

	# test verb/object with 2 adjectives
	command = lexicon.classify([('verb', 'take'), ('adjective', 'big'), ('adjective', 'red'), ('noun', 'key')])
	assert_equal(command.verb.name, 'take')
	assert_equal(command.object.name, 'key')
	assert_equal(command.object.modifiers, ['red', 'big'])
	
	
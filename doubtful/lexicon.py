WORD_TYPES = {
	'verb' : ['go', 'use', 'eat', 'look', 'get', 'check', 'drink', 'talk', 'take', 'pick', 'listen'],
	'direction' : ['north', 'south', 'east', 'west', 'up', 'down', 'left', 'right'],
	'noun': ['door', 'key', 'man', 'woman', 'trinket', 'glasses', 'table', 'apple', 'song'],
	'adjective': ['red'],
	'preposition': ['on', 'under', 'from', 'to', 'behind'],
	'stop': ['the', 'in', 'of'],
	'article': ['a', 'an', 'the'],
	'command': ['status', 'help', 'map'],
	'extra': ['exit', 'save', 'load', 'reset']
}

VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}

class Command(object):
	def __init__(self, verb):
		self.verb = verb
		self.object = None

class Verb(object):
	def __init__(self, name):
		self.name = name

class Object(object):
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.modifiers = []

class Lexicon(object):

	def preprocess(self, sentence):
		return sentence.lower()

	def scan(self, sentence):
		tokens = []
		for word in sentence.split():
			try:
				word_type = VOCABULARY[word]
			except KeyError:
				try:
					value = int(word)
				except ValueError:
					tokens.append( ('error', word))
				else:
					tokens.append( ('int', value))
			else:
				tokens.append( (word_type, word))
		return tokens
		
	def clean(self, tokens):
		clean_tokens = tokens
		for token in clean_tokens:
			if token == ('article', 'an') or token == ('article', 'a'):
				clean_tokens.remove(token)
		return clean_tokens

	def classify(self, tokens):
		command = False
		if tokens[0][0] == 'verb':
			command = Command(Verb(tokens[0][1]))
			for token in tokens[0:]:
				
				if token[0] == 'noun':
					object = Object(token[1], 'direct')
					command.object = object
					# check for adjective:
					if tokens[tokens.index(token) - 1][0] == 'adjective':
						object.modifiers.append(tokens[tokens.index(token) - 1][1])
			
		return command

	def parse(self, sentence):
		output = self.preprocess(sentence)
		output = self.scan(output)
		output = self.clean(output)
		return output

def return_verbs():
	verb_list = []
	for word in WORD_TYPES['verb']:
		verb_list.append(word)
	return verb_list
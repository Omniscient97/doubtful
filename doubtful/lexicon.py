WORD_TYPES = {
	'verb' : ['go', 'use', 'eat', 'look', 'get', 'check', 'drink', 'talk', 'take'],
	'direction' : ['north', 'south', 'east', 'west', 'up', 'down', 'left', 'right'],
	'noun': ['door', 'key', 'man', 'woman', 'trinket', 'glasses'],
	'preposition': ['on', 'under'],
	'stop': ['the', 'in', 'of'],
	'article': ['a', 'an'],
	'command': ['status', 'help'],
	'extra': ['exit', 'save', 'load', 'reset']
}

VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}

class Lexicon(object):

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
		
	def parse(self):
		pass

def return_verbs():
	verb_list = []
	for word in WORD_TYPES['verb']:
		verb_list.append(word)
	return verb_list
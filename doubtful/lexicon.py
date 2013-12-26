WORD_TYPES = {
	'verb' : ['go', 'use', 'eat', 'look', 'get', 'check', 'drink', 'talk', 'take', 'pick', 'listen'],
	'direction' : ['north', 'south', 'east', 'west', 'up', 'down', 'left', 'right'],
	'noun': ['door', 'key', 'man', 'woman', 'trinket', 'glasses', 'table', 'apple', 'song'],
	'preposition': ['on', 'under', 'from', 'to'],
	'stop': ['the', 'in', 'of'],
	'article': ['a', 'an'],
	'command': ['status', 'help', 'map'],
	'extra': ['exit', 'save', 'load', 'reset']
}

VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}

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

	def parse(self, sentence):
		return self.clean(self.scan(self.preprocess(sentence)))

def return_verbs():
	verb_list = []
	for word in WORD_TYPES['verb']:
		verb_list.append(word)
	return verb_list
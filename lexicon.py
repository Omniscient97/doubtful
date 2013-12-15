print('Enter commands into the prompt.')

lexicon = {'go': 'verb', 'open': 'verb', 'north': 'direction', 'south': 'direction',
'east': 'direction', 'west': 'direction'}


user_input = input('> ')
words = user_input.split()
output_words = []
for word in words:
	if word in lexicon:
		output_words.append((word, lexicon[word]))
	else:
		output_words.append(word, 'error')
print(output_words)
input('press enter to exit ;)')
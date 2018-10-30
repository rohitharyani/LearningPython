def hello(name):
	print('Hello, '+ name)


hello('Rohit')

#---------------------------
#Pig latin encryption
def pig_latin(word):
	'''
	Convert any word to a secret pig latin word.
	'''
	firstLetter = word[0]
	if firstLetter in 'aeiou':
		pig_word = word+'ay'
	else:
		pig_word = word[1:]+firstLetter+'ay'


	return pig_word


print(pig_latin('hello'))
import math 

def volume(radius):
	'''
	Calculate volume of a sphere based on the formula
	'''
	return (4.0*math.pi*(radius**3))/3

print("Volume of sphere is: ",volume(3))

#-----------------------------------


def valueInRange(num,low,high):
	'''
	Check for a given value in a defined range
	'''
	return "Value in range" if num in range(low,high+1) else "Value not in range"
		
print(valueInRange(3,1,10))

#------------------------------------

def up_low(sentence):
	'''
	Count the number of upper and lower case characters in a given string
	'''
	d={"upper":0, "lower":0}
	for c in sentence:
		if c.isupper():
			d["upper"]+=1
		elif c.islower():
			d["lower"]+=1
		else:
			pass

	print("Upper: ",d["upper"])
	print("Lower : ",d["lower"])


sentence = "Hello, my name is Rohit Haryani"
print(sentence)
up_low(sentence)
#------------------------------------

def unique(list):
	'''
	Display the unique values in a list
	'''
	answer = set()
	for i in list:
		answer.add(i)
	return answer

sample = [1,1,1,2,3,3,6,6,6,5,5,5,8,8,8,9]
print("Unique elements of the list are: ",list(unique(sample)))


#-------------------------------------------

def multiply(list):
	'''
	Calculate the multiplication of the elements of a list
	'''
	answer = 1
	for i in list:
		answer*=i

	return answer

sample1 = [1,2,3,-4]
print("Multiplication of list is: ", multiply(sample1))

#-------------------------------------------

def palindrome(sentence):
	'''
	Check if a string is a palindrome
	'''
	return "Palindrome" if sentence == sentence[::-1] else "Not a palindrome"

sentence = "helleh"
print(palindrome(sentence))

#--------------------------------

import string

def isPangram(sentence, alphabet=string.ascii_lowercase):
	'''
	Check if string is a panagram
	'''
	alphaset = set(alphabet)
	return "Is Pangram" if alphaset <= set(sentence.lower()) else "Not a Pangram"

sentence = "abcdefghijklmnopqrstuvwxxyz"
print(isPangram(sentence))
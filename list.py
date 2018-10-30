#Understanding how lists work in python
myList = []
myString = "hello"

for letter in myString:
	myList.append(letter)

print(myList)
#----------------------------

myList = [letter for letter in myString]

print(myList)

#Global string
x = 25

def printer():
	#Local variable
	#Function will return loacal variable
	x = 50
	return x

print(printer())

#------------------------------

name = 'This is a global string'

def greet():
	#GLOBAL Keyword makes the variable use global attributes
	#Thus prints global string
	global name

	def hello():
		print('Hello '+ name)

	hello()

greet()

#------------------------------



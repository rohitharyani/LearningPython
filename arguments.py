def myfunc(*args):
	'''Pass in arbitary number of parameters.
	No need to worry about the number or type.
	'''
	print(sum(args))


myfunc(20,3,0,6,6,6,5)

#-------------------------------------------------

def myfunc1(**kwargs):
	'''
	Pass in dictionary.
	Multiple key word arguments can be passed. 
	Returns back a dictionary.
	'''
	if 'fruit' in kwargs:
		print("My fruit of choice is {}.".format(kwargs['fruit']))
	else:
		print("No fruit of my choice!")

myfunc1(fruit='apple')

#--------------------------------------------------------

def myfunc2(*args, **kwargs):
	print('I would like to order {} {}.'.format(args[0], kwargs['food']))

myfunc2(10,20,30,food="Butter Chicken")
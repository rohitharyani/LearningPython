
#Map applies a function to all the items in a input
def square(num):
	'''
	Function to square numbers
	'''
	return num**2


my_nums = [1,2,3,4,5]
#Print list of squared numbers
print(list(map(square, my_nums)))
	
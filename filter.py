#Filter creats a list of items for which the return value is true based on a function
def check_even(num):
	'''
	Return True if a number is even
	'''
	return num%2==0


numbers = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(check_even, numbers)))
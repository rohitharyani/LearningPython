#Lambda expression is a function without a name to execute only once 
numbers = [50,2,3,5]
square = lambda num: num**2

print(square(2))

print(list(map(lambda num: num**2, numbers)))
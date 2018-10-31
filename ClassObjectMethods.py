myList = [1,2,3]
mySet = set()

class Dog():
	#Class object attribute
	species = "Mammal"
	def __init__(self, breed, name):
		self.breed = breed
		self.name = name

	#Method
	def barks(self,number):
		print("Woof! My name is {} and the number is: {}".format(self.name,number))

my_dog = Dog('Lab','scotchy')
my_dog.barks(10)
print(my_dog.species)

#-------------------------------------------------------

class Circle():
	#Class object attribute
	pi = 3.14

	def __init__(self, radius=1):
		self.radius = radius
		self.area = Circle.pi*(radius**2)

	#Method to return circumference up to 2 decimal digits
	def get_circumference(self):
		return round(self.radius * self.pi *2,2)

	def get_area(self):
		return self.area
my_circle = Circle(6)
print(my_circle.get_circumference())
print(my_circle.get_area())
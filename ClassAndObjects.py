myList = [1,2,3]
mySet = set()

class Dog():
	species = "Mammal"
	def __init__(self, breed, name):
		self.breed = breed
		self.name = name


	def barks(self,number):
		print("Woof! My name is {} and the number is: {}".format(self.name,number))

my_dog = Dog('Lab','scotchy')
my_dog.barks(10)
print(my_dog.species)


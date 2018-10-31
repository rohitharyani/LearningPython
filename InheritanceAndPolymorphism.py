#Inheritance
class Animal():
	def __init__(self):
		print("Animal Created")

	def who_am_i(self):
		print("I am an Animal")

	def eat(self):
		print("I am eating")

class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Dog Created")

	def who_am_i(self):
		print("I am a dog")
	
	def bark(self):
		print("Woof!")

my_animal = Animal()
my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()

#----------------------------------------
#Polymorphism
class Dog():
	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says woof!"

class Cat():
	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " says meow!"


niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
	print(type(pet))
	print(pet.speak())


def pet_speak(pet):
	print(pet.speak())

pet_speak(niko)
pet_speak(felix)


#---------------------------------
#ERROR

class AnimalBase():
	def __init__(self,name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Subclass must implement this abstract method!")


class Doggy(AnimalBase):
	def speak(self):
		return self.name + " says woof!"

fido = Doggy('Fido')
print(fido.speak())
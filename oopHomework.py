#------------------------------------------------------------------------------------------
#Problem 1 - Find the distance and slope between 2 lcoordinates
class Line:
	def __init__(self,coo1,coo2):
		(self.coo1x,self.coo1y) = coo1
		(self.coo2x, self.coo2y)= coo2

	def distance(self):
		return (((self.coo2y-self.coo1y)**2 + (self.coo2x-self.coo1x)**2)**0.5)

	def slope(self):
		return self.coo2y-self.coo1y/self.coo2x-self.coo1x


coordinate1 = (3,2)
coordinate2	= (8,10)

li = Line(coordinate1,coordinate2)

print(f"The distance between {coordinate1} and {coordinate2} is {li.distance()} units")
print(f"The slpoe of the line is {li.slope()} units")

#-------------------------------------------------------------------------------------------
#Problem 2  - Find the volume and surface area of a cylinder
import math
class Cylinder:
	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		return round(math.pi*self.height*(self.radius**2),2)

	def surface_area(self):
		return round((2*math.pi*self.height*self.radius) + (2*math.pi*(self.radius**2)),2)

height = 2
radius = 3

cy = Cylinder(height,radius)
print(f"Volume of a cylinder for height = {height} and radius = {radius} is {cy.volume()} cq.unit")
print(f"Surface area of a cylinder for height = {height} and radius = {radius} is {cy.surface_area()} sq.unit")
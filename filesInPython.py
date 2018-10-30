myfile = open('filesInPython.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()

with open('filesInPython.txt', mode='a') as myfile:
	myfile.write("\nHi Rohit")


myfile = open('filesInPython.txt')
print(myfile.read())

#-------------Lists-------------------
myList = ['one','two','three']
print(myList)

#Add to the end of the list
myList.append('four')
print(myList)

#Remove item from the list
myList.pop()
print(myList)


print(myList)


#----------------Dictionaries-----------------

myDict = {'key1':{'value1':'10'},'key2':'value2'}
print(myDict['key1']['value1'])


#----------------Tuples--------------------

myTuple = (1,'two',3,5)
myList = [1,2,3]
print(myTuple.index(3))

#-----------Sets----------------------------

mySet = set()
mySet.add(1)
mySet.add(12)
mySet.add(13)
mySet.add(1)
mySet.add(4)
print(mySet)
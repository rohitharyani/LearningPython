#-----------------------------------
#Range
for num in range(3,10,2):
	#range(start,until, jump)
	print(num)

#-----------------------------------
#Enumerate
for index,letter in enumerate('abcde'):
	print(f"{index} {letter}")


#-----------------------------------
#Zip - only the shortest of the two lists is zipped. 
#Rest will be ignored

list1 = [1,2,3]
list2 = ['a','b','c']

for item in zip(list1,list2):
	print(item)

#-----------------------------------
#In operator

print('a' in 'abcde')

#-----------------------------------
# Min and Max

list1 = [1,2,3,4,5,6]
print(min(list1))
print(max(list1))

#-----------------------------------
#Random library 

from random import shuffle
list1 = [1,2,3,4,5,6,7,8,9,10]
shuffle(list1)
print(list1)


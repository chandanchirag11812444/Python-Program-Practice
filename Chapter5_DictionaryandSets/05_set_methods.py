#Creating an empty Set 
b=set()
#Adding values to Empty set
print(type(b))
b.add(10)
b.add(20)
b.add(10)#adding a value repeateadly cannot change the value in set and will not repeat
b.add((5,8,9))#We can add tuples in a set
# b.add({4:5})#can add list or dictionary in a set


b.add(50)
print(b)
##length of the set
print(len(b))#print the lenght of the set
##Removal of the item
# b.remove(5)#remove 5 from the set b
#as 5 is not present in set so it will throws an error 
b.remove(10)
#it will remove 10 from set 
print(b)
print(b.pop())#randomally remove number in set
print(b)


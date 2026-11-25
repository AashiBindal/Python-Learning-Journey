#sets

#A set is an unordered collection of items. 
#Every set element is unique. No duplicates. 
#and must be immutable, cannot be changed. 
#However, a set itself is mutable. We can add or remove  items from it. 
#Sets can also be used to perform mathematical set operations like union, intersection, symmetric differences, etc. 

#Characteristics are:
#- unordered
#- mutable
#- no duplicates
#- can't contain mutable data types

s= {} #dict

# empty set
s=set()
print(s)
print(type(s))

#1d 2d
s1={1,2,3}
print(s1)

#2d -> not possible 
#s2={1,2,{3}}
#print(s2)

#homo hetro
s={1,1,4,5,5}
S={1,1.3,'hi' , True} #true=1
print(s,S)

#using type convertion
a=set([1,2,3])
print(a)

#duplicates not allowed
d={1,2,1,2,11,1}
print(d)

# sets cant have mutable items 
#s={1,2,[3,4]} #error

#unorderd
s1={1,2,4}
s2={2,4,1}
print(s1==s2)

#accessing items are not allowed
#indexing X
#slicing X
#editing X

#adding and deleting

#add -> one item at a time 
s={1,2,3 ,5}
s.add(4)
print(s)

#update -> multiple items at a time
s={1,2,3 ,5}
s.update([6,7,8])
print (s)

#DELETING ITEMS

#del -> delete whole set
#x={1,2}
#del(x)
#print(x)

#discard->error show nhi hoga if item present nhi h
s={1,2,3 ,5}
s.discard(5)
print(s)

#remove->error show hogaa if item present nahi h to
s={1,2,3 ,5}
s.remove(2)
print(s)

#pop->dlt random item
s={1,2,3 ,5}
print(s.pop())

#clear->empty
s={1,2,3 ,5}
print(s.clear())

#--------------------------------------------------
#--------------------------------------------------

set = {3,1,4,5,8,9,0}

# len
print(len(set))

# sum
print(sum(set))

# min
print(min(set))

# max
print(max(set))

# sorted
print(sorted(set))
print(sorted(set , reverse= True))

# union
print(set.union({10,11}))

s1 = {2 , 6 , 8}
s2 = {1 , 3 , 5}
print(s1.union(s2))

# update
set.update({10,11})
print(set)

s1 = {2 , 6 , 8}
s2 = {1 , 3 , 5}
s1.update(s2)
print(s1)
print(s2)

# intersection
s1 = { 1 , 5 , 2 , 6 , 8}
s2 = {1 , 3 , 5}
print(s1.intersection(s2))

# intersection_update
s1 = { 1 , 5 , 2 , 6 , 8}
s2 = {1 , 3 , 5}
print(s1.intersection_update(s2))
print (s1)
print(s2)

# difference
s1 = { 1 , 5 , 2 , 6 , 8}
s2 = {1 , 3 , 5}
print(s1.difference(s2))

# difference_update
s1 = { 1 , 5 , 2 , 6 , 8}
s2 = {1 , 3 , 5}
print(s1.difference_update(s2))
print (s1)
print(s2)

# symmetric_difference
s1 = { 1 , 5 , 2 , 6 , 8}
s2 = {1 , 3 , 5}
print(s1.symmetric_difference(s2))

# symmetric_difference_update
s1 = { 1 , 5 , 2 , 6 , 8}
s2 = {1 , 3 , 5}
print(s1.symmetric_difference_update(s2))
print (s1)
print(s2)

# isdisjoint -> check every items of both sets are different 
a = {1,2,3,4,5}
b = {1,7,8,9,0}
print(a.isdisjoint(b))

# issubset -> check if all items of set1 are present in set2 
s1 = {1,2,3,4,5}
s2 = {3,4,5}
print(s2.issubset(s1))

s1 = {1,2,3,4,5}
s2 = {3,4,5}
print(s1.issubset(s2))


# issuperset -> check if all items of set2 are present in set1
s1 = {1,2,3,4,5}    
s2 = {2,4}
print(s1.issuperset(s2))

# copy 
c1 = {1,2,3}
c2 = c1.copy()
print(c2)

#--------------------------------------------------------------
#--------------------------------------------------------------

# FROZEN SETS -> Frozen set is just an immutable version of a Python set object. 

# Create a frozen set. 
fs = frozenset([1,2,3])
print (fs)

fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])
print(fs1.union(fs2))

# addition , update , remove , discard , pop , clear are not possible in frozen sets as they are immutable.
# works -> all read functions 
# does't work -> write operations

#when to use -> 2d sets 
fs = frozenset([1,2,frozenset([5,7])])
print(fs)

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

# set comprehension 

print({i for i in range (1,11)})

print({i for i in range (1,11) if i%2==0})

print({i**2 for i in range (1,20) if i%2==0})
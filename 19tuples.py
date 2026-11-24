# TUPLES 

# A tuple in Python is similar to a list. The difference between the two is that we cannot change 
#  The elements of a tuple, once it is assigned, whereas we can change the elements of a list 

# A tuple is an immutable list. A tuple cannot be changed in any way  once it is created. 

# Characteristics 
# Ordered, unchangeable, allow duplicates. 

#creating tuples
#empty
t1=()
print(t1)
#Create a tuple with a  single item
t2=('123',)
print(type(t2))
print(t2)
#homo
t3=(1,2,3,4)
print(t3)
#hetro
t4=(1,2.2,'hello',1+7j,[1,2,3])
print(t4)
#2d,3d,,,
t5=(1,2,3,(4,'5'),(2,3,('i')))
print(t5)
#using type con
t6=tuple('hello')
print(t6)
#--------------------------------------.
#accessing items
#indexing
print(t3)
print(t3[2])
print(t3[-1])
#slicing
print(t3[0:3])
print(t5[-1][0])
#---------------------------------------
#tuples are immutable just like strings 
#editing , addition are not possible
#we can delete a whole tuple but not a part of it
t7=(1)
del(t7)
#---------------------------------------
#operations 
#arithmetic
t1=(1,2)
t2=(2,3)
print(t1+t2)
print(t1*2 +  t2*2)
#membership
print(1 in t1 )
print(2  not in t2)
#iteration
for i in t1:
    print(i)
#----------------------------------------
a=(4,35,245,6,0,-1,-1)
# len 
print(len(a))
# sum
print(sum(a))
# max
print(max(a))
# min
print(min(a))
# sorted
print(sorted(a))
print(sorted(a,reverse=True))
# count    -> frequency count
print(a.count(-1))
#index
print(a.index(245))
#---------------------------------------
#tuples are faster in speed then list
import time
L=list(range(100000))
T=tuple(range(100000))
start=time.time()
for i in L:
    i*5
print('list time' , time.time()-start)

start=time.time()
for i in T:
    i*5
print('TUPLE time' , time.time()-start)  
#-------------------------------------
#tuples use less memory comparatively
import sys
L=list(range(1000))
T=tuple(range(1000))
print('list size : ' , sys.getsizeof(L))
print('tuple size : ' , sys.getsizeof(T))
#--------------------------------------
#tuple unpacking
a,b,c=(1,2,3)
print(a,b,c)
#--------------
#swaping
a=1
b=2
a,b = b,a
print(a,b)
#--------------
a,b,*others = (1,2,3,4,4)
print(a,b)
print(others)
#-----------------------------------------
#zip function
t1=(1,2,3)
t2=(2,2,2)
print(tuple(zip(t1,t2)))
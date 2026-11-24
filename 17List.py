# Lists are mutable. 

a=[1,2,3] # order matter 
b=[2,1,3]
print(a==b)
#--------------------------------
#CREATE LIST 

#empty list 
print([])
#1D
print([1,2,3,4,5,5])
#2D->hetro
print([1,2,3,[4,5]])
#3D
print([1,2],[3,4,4],[[5,5,6],[1]])
#hetrogeneous
print([1,True , 'aashi ' , 5+6j , 4.44] )
#using type conversion
print(list('hello'))
#--------------------------------------
#accessing items from a list

#indexing
#positive 
l=[1,2,3,4,5]
print(l[0])
#negative
l=[1,2,3,4,5]
print([l[-1]])

#2d 
a=[1,2,3,[4,5]]
print(a[3][1])

#3D
b=[[1,2],[3,4,4],[[5,5,6],[1]]]
print(b[2][0][2])

#slicing
l=[1,2,3,4,5,6]
print(l[0:3])
l=[1,2,3,4,5,6]
print(l[0::2])
l=[1,2,3,4,5,6]
print(l[::-1])
#--------------------------------------
#adding items to a list 

#append -> add one element in the end of a list
a=[1,2,3,4,5]
a.append('a')
print(a)

a=[1,2,3,4,5]
a.append([6,7,8])
print(a)

#extend ->add multiple items simultaneously
a=[1,2,3,4,5]
a.extend([6,7,8])
print(a)

a=[1,2,3,4,5]
a.extend('delhi')
print(a)

#insert->add in random index
a=[1,2,3,4,5]
a.insert(1,100)
print(a)

#----------------------------------------------

#EDITING ITEMS IN THE LIST

#editing with indexing 
L=[1,2,3,4,5]
L[-1]=500
#editing with slicing
L[1:4] =[200,300,400]
print(L)

#---------------------------------------------

#DELETION ITEMS FROM A LIST 

#DEL
#L=[1,2,3,4,5] 
#del[L]
#print(L)

L=[1,2,3,4,5]
del L[-1]
del L[1:3]
print(L)

#REMOVE->use when we dont know , in which index item is store
L=[1,2,3,4,5]
L.remove(4)
print(L)

#POP->default delete last  item otherwise dlt with index
L=[1,2,3,4,5]
L.pop()
print(L)

L=[1,2,3,4,5]
L.pop(2)
print(L)

#CLEAR->dlt all items not list
L=[1,2,3,4,5]
L.clear()
print(L)

#----------------------------------------------

#arthmetic(+,*)
L1 = [1,2,3]
L2 =[4,5]
print(L1+L2) #concatenation/merge

print(L1*3) # print L1 three times

#membership
l1 =[1,2,3,4,5,6]
print(5 in l1)
l2 =[1,2,3,[4,5]]
print([4,5] in l2)
l2 =[1,2,3,[4,5]]
print(5 not in l2)

#loop
l1 =[1,2,3,4,5,6]
for i in l1:
    print(i)
l2 =[1,2,3,[4,5]]
for i in l2:
    print(i)
l3 =[1,2],[3,4,4],[[5,5,6],[1]]
for i in l3:
    print(i)

#-----------------------------------------------

#FUNCTIONS

L=[2,1,1,3,3,3,7,0,9]
#len
print(len(L))
#min
print(min(L))
#max
print(max(L))
#sorted->temp sorting
print(sorted(L))
#reverse sorting
print(sorted(L,reverse=True))
#count->count frequency
print(L.count(3))
#index 
print(L.index(0))
#reverse->permanently reverse the list 
a=[1,34,43,3,333,30]
a.reverse()
print(a)
#sort->permanently sorting 
a=[1,34,43,3,333,30]
print(sorted(a))
print(a)
a.sort()
print(a)
#copy 
L=[2,3,4,5]
print(L)
print(id(L))
L1=L.copy()
print(L1)
print(id(L1))

#zip 
# The `zip` functions return a `zip` object, which is an iterator of tuples where the first item in each pair is paired
# Together And then the second item in each parser iterator is paired together. 
#If the passed Iterators have different lengths. The iterator with the least item decides the length of the new iterator. 
L1 = [1,2,3,4]
L2 =[-1,-2,-3,-4]
list(zip(L1,L2))
l=[i+j for i,j in zip(L1,L2)]
print(l)

#lists are flexible
l=[1 , 3, print , input , zip ]


# Two ways to traverse a list 
#Item-wise 
l = [1,2,3,4,5]
for i in l :
    print(i)
#Index-wise 
l = [1,2,3,4,5] 
for i in range(0,len(l)):
    print(i) #l[i]->for prining the value of item

#disadvantages of list
# slow
# risky usage 
# eats up more memory 






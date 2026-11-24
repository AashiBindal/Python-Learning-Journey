#List comprehension Provides a concise way of creating lists. 

#New list = [expression for item in iterable if condition == True]

#Advantage of list comprehension 
#more time-efficient and space-efficient than loops 
#Require fewer lines of code. 
#Transforms an iterative statement into a formula. 

#print 1 to 10
L=[]
for i in range(1,11):
    L.append(i)
print(L)    
#---list comprehension
L=[i for i in range(1,11)]
print(L)
#scalar multiplication on a vector
v=[1,2,3]
s=-3

x=[]
for i in v:
    x.append(i*s)

print(x)    
#--list comprehension
v=[1,2,3]
s=-3
x=[]
x=[s*i for i in v]
print(x)

#add square
L=[2,3,4,5,6,7]
s=[i**2 for i in L]
print(s)

#print all numbers divisible by 5 in the range of 1 to 50
d=[i for i in range (1,51) if i%5==0]
print(d)

#find language which start with letter p
languages = ['java' , 'python' , 'php' , 'c' , 'javascript']
l=[language for language in languages if language.startswith('p')]
print(l)

#nestedd if with list comprehension
basket=['apple' , 'guava' , 'cherry' , 'banana']
my_friuts=['apple','kivi','graphs','banana']

#add new list from my_friuts and items if the fruit exists in basket and also starts with 'a'

f=[fruit for fruit in my_friuts if fruit in basket if fruit.startswith('a')]
print(f)

#print a (3,3) matrix usinf list-com
x=[[i*j for i in range (1,4)]for j in range(1,4)]
print(x)

#cartesian products
L1 = [1,2,3,4]
L2 = [5,6,7,8]
c=[i*j  for i in L1 for j in L2]
print (c)

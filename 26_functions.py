# FUNCTIONS 
# two main principle : abstraction , decomposition 

def is_even (i) :
    '''
    input : i , a positive int 
    returns true if i is even , othervise false 
    '''
    print("inside is_even")
    return i%2 == 0
print(is_even(7))
print(is_even(8))

# def -> keyword 

# is_even -> fun name 

# i -> parameter / argument 

#print("inside is_even")
  #  return i%2 == 0       -> body             

#print(is_even(7))
#print(is_even(8))     -> calling 

#'''
 #   input : i , a positive int 
  #  returns true if i is even , othervise false 
   # '''                                               -> docstring

print(is_even.__doc__)
print(print.__doc__)


#-----------------------------------------------------------------------------------------


def is_odd (num) :
    """
    check the number is odd or not 
    """
    if num % 2 != 0 :
       return "odd"
    else :
       return "even"


for i in range(1,21) :
   x = is_odd(i)
   print(x)    

#---------------------------------------------------------------------

# safe side 
def is_odd (num) :
    """
    check the number is odd or not 
    """
    if type(num) == int :
        if num % 2 != 0 :
         return "odd"
        else :
         return "even"
    else :
        return "only integer !! "

print(is_odd("hello"))    


#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


# Types of arguments:

# default argument

def power(a=1 , b=1):
   return a**b
print(power(4,2))
print(power(5))
print(power())


# positional argument

print(power(9,2)) 


# keyword argument

print(power(b=3,a=2))


#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


# (*args) and  (**kwargs)  :   are special Python keywords that are used to pass the variable length of arguments to a function. 

# *args (its not compulsory to only use word args we can use any word)
         #Args allow us to pass a variable number of non-keyword arguments to a function. 

#multiply n numbers
def mul(*args):
   product = 1 

   for i in args:
    product = product * i 

   return product  

print(mul(1,3,5,10))
print(mul(9,2,3,4,4,4,2))

# **kwargs -> Allow us to pass any number of keyword arguments. 
           # Keyword arguments mean that they contain a key-value pair, like a Python dictionary. 

def display (**kwargs):

   for (key,value) in kwargs.items():
      print  (key , '->' , value)

display(india = 'delhi' , srilanka = 'colombo' , nepal = 'kathmandu' , pakistan = 'islamabad')     

## Points to remember while using `args` and `kwargs` 
   ## The order of the arguments matters. (normal -> *args -> **kwargs)
   ## The words `args` and `kwargs` are only a convention. You can use any name of your choice. 


#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------


# GLOBAL AND LOCAL SCOPE

# 1. Local Scope
# A variable declared inside a function is called a Local Variable.
# It can be accessed only inside that function.
# It cannot be directly accessed outside the function.
# It exists during the function's execution (for ordinary local variables).

                                                                                                                                                                                            

#2. Global Scope
#A variable declared outside all functions is called a Global Variable.
#- It can be accessed inside and outside functions.
#- It can be accessed by multiple functions.
#- To modify a global variable inside a function, we generally use the global keyword.

def g(y):
   print(x)
   print(x+1)
x=5
g(x)
print(x)   

#-----------------------------------

def f(y) :
   x=1
   x+=1
   print(x)
x=5
f(x)
print(x)   

#-------------------------------------

def h(y):
   global x
   x+=1
x=5
h(x)
print(x)   

#---------------------------------------

def f(x):
   x+=1
   print('in f(x) : x = ' , x)
   return x

x = 3
z = f(x)
print('in main program scope : z =' , z)
print('in main program scope : x =' , x)


#------------------------------------------
#------------------------------------------

## NESTED FUNCTION 


def f():
   def g():
      print('inside fun g')
   g()
   print('inside fun f') 
f()  

#------------------------------------------

def g(x):
   def h():
      x='abc'
   x+=1
   print('in g(x): x =' , x )
   h()
   return x

x=3
z=g(x)

#------------------------------------------


def g(x):
   def h(x):
      x+=1
      print("in h(x) : x = " , x)
   x+=1
   print('in g(x) : x = ' , x)
   h(x)
   return x

x=3
z=g(x)
print('in main program scope : x = ' , x)
print('in main program scope : z = ' , z)

#-------------------------------------------
#-------------------------------------------

# function in python is act as a datatype 
#(functions are 1st class citizens )

#type and id
def square(num):
   return num**2

print(type(square))
print(id(square))


#reassign
x= square
print(x)
print(x(3))


#storing 
l=[1,2,3,4,square]
print(l)
print(l[-1](5))


# deleting a function 
def cube(a):
   return a**3
#del cube(3)


# returning a function 
def f():
   def x(a,b):
      return a+b 
   return x
val = f()(5,5)
print(val)


# function as argument 
def fun_a():
   print('inside fun_a')

def fun_b (z):
   print('inside fun_b')
   return z()

print(fun_b(fun_a))   #z= fun_a


#---------------------------------------------------------
#---------------------------------------------------------


#Benefits of using a function:
#- Code modularity
#- Code readability
#- Code reusability


#---------------------------------------------------------
#---------------------------------------------------------


# lambda function 

# A lambda function is a small anonymous function. 
# A lambda function can take any number of arguments but can only have one expression. 

#syntax
lambda a,b : a+b

# x -> x*2
a = lambda x : x**2
print(a(6))

#x,y -> x*y
b = lambda x,y,z : x*y*z
print(b(4,5,6))

#Difference between lambda and a normal function:
#- No name
#- Lambda has no written value (infact , return a function )
#- Lambda is written in one line
#- Not reusable

#Then why use lambda functions? 
#->>> They are used with HOF (higher order fun). 


# check if a string has 'a'
c = lambda s : 'a' in s
print(c('asjrbainsoinureu'))

#odd or even
d = lambda num : 'even' if  num%2==0 else 'odd'
print(d(98384782))

#-----------------------------------------------

## HIGHER ORDER FUNCTION 
 # FUNCTION RETURNS A FUNCTION OR RECIEVE A FUNCTION IN INPUT 


def square(x):
   return x**2

#hof
def transform(f,L):
   output = []
   for i in L:
      output.append(f(i))

   print(output)

L = [1,2,3,4,5]

transform(lambda x : x**2 , L)
transform(lambda x : x**3 , L)

#----------------------------------------------------------

#MAP 
 #map accept lambda or iterable list

# Square the item of the list. 
print(list(map(lambda x : x**2 , [1,2,3,4,5]) ))

# odd/ even labeling of list item 
L=5,6,8,5,4,0,9,1
print(list(map(lambda x: 'even' if x%2==0 else 'odd' , L)))


#Fetch name from a list of dict.


users = [
    {
        'name': 'Rahul',
        'age': 45,
        'gender': 'male'
    },
    {
        'name': 'Nitish',
        'age': 33,
        'gender': 'male'
    },
    {
        'name': 'Ankita',
        'age': 50,
        'gender': 'female'
    }
]

print(list(map(lambda users : users['name'] , users)))


#-------------------------------------------------------------------------


#FILTERS
 #-> filter acc to the condition 

#number greator than 5
L = [5,63,3,2,7,9,997,75,0,1]
print(list(filter(lambda x : x>5 , L)))


#Fetch fruits starting with A. 
fruits = ['apple' , 'banana' , 'cherry']
print(list(filter(lambda x : x.startswith('a') , fruits)))



#-------------------------------------------------------------------------


# REDUCE
 # import functools 

import functools

# Sum of all items 
print(functools.reduce(lambda x,y : x+y ,[1,2,3,4,5]))


#find mmin
print(functools.reduce(lambda x,y : x if x<y else y ,[3,44,5,-9,7,-66] ))


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------








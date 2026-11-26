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

#----------------------------------------------------------------


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

#------------------------------------------------------------------


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

























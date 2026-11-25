#  dictionary 

# dictionary in python is a collection of keys values 
# used to Store data values like a map, unlike other data types, which hold only a single value as an element. 

#In some languages, it is known as a map or associative arrays.

d = {'name' : 'aashi' , 'age' : 20 , 'gender' : 'male'}

# Characteristics:
#- Mutable 
# -indexing has no meaning.
#- Keys can't be duplicated.
#- Keys can't be mutable items. 

#empty dictionary
dict1 = {}
print(dict1)

#1D dictionary 
dict2 = {'name': 'aashi', 'age': 20, 'gender': 'male'}
print(dict2)

#with mixed keys 
dict3 = {(1,2,3):1 , 'hello' : 'world'}
print(dict3)

#2D dictionary 
student = {
         'name' : 'aashi' ,
         'collage' : 'acropolis' ,
         'sem' : 5 ,
         'subjects' : {
             'dsa' : 100,
             'python' : 99 ,
             'english' : 99 
         }

}
print(student)

#using sequence and dict functions 
dict4 = dict([(1,1),(2,4),(3,9)])
print(dict4)

dict5 = dict.fromkeys(['a','b','c'], 0)
print(dict5)

dict6 = dict([('name', 'aashi'), ('age', 20), ('gender', 'female') , ('number' , 7225910911)])
print(dict6)

#can not have duplicate keys
dict7 = {'name' : 'ashi' , 'name' :'aashi'}
print(dict7) # it will print the last value of the key 'name' which is 'aashi'

#mutuable keys are not allowed
#dict8 = {[1,2,3] : 'value'} # it will give error because list is mutable and can not be used as key in dictionary

#--------------------------------------------------------------------------------------------------------------------------


#Accessing items in dictionary  -> indexing / slicing are not allowed in dictionary because it is unordered collection of items.

#1 []
dict9 = {'name' : 'aashi' , 'age' : 20}
print(dict9['name']) # it will print the value of the key 'name' which is 'aashi'
print(dict9['age']) # it will print the value of the key 'age' which is 20

#2 get() method
dict10= {'name' : 'aashi' , 'age' : 20}
print(dict10.get('name')) # it will print the value of the key 'name' which is 'aashi'
print(dict10.get('age')) # it will print the value of the key 'age' which is 20


print(student['subjects']['dsa']) # it will print the value of the key 'dsa' which is 100


#-----------------------------------------------------------------------------------------------


#adding new key-value pair 
dict10= {'name' : 'aashi' , 'age' : 20}
dict10['weight'] = 51.8 
print(dict10) # it will print the dictionary with new key-value pair added

student['subjects']['maths'] = 100
print(student)


#-----------------------------------------------------------------------------------------------


#Remove key-value pair

dict11= {'name' : 'aashi' , 'age' : 20 , 'gender' : 'female' , 'weight' : 51.8}

#pop -> remove the key-value pair with the specified key and return the value
print(dict11.pop('gender')) # it will remove the key-value pair with the key 'gender' 

#popitem -> delete last key value pair
print(dict11.popitem())

#del -> remove the key-value pair with the specified key
del dict11['age']
print(dict11)

#clear
print(dict11.clear()) # it will remove all the key-value pairs from the dictionary and return an empty dictionary


del student['subjects']['english'] # it will remove the key-value pair with the key 'english' from the nested dictionary

#-------------------------------------------------------------------------------------------------------------------------------


#Editing key-value pair

student['sem'] = 'V'
print(student)
student['subjects']['python'] = 100
print(student)

#---------------------------------------------------------------------------------------------------------------------------------


# Dictionary comprehension 

#{key : value for variable in iterable}

# print 1st 10 no. with their cubes 
print({i : i**3 for i in range(1,11)})


#using existing dictionary 
distance = {'delhi' : 1000 , 'mumbai' : 2000 , 'banglore' : 3000}
print({key : value*0.5 for (key,value) in distance.items()}) 


#using zip 
days = ['sunday' , 'monday' , 'tuesday' 'wednesday' , 'thursday' , 'friday' , 'saturday']
tem_c = [30.5 , 32.4 , 44.1 , 55.5 , 20.1 , 30.1 , 09.1]
print({i:j for(i,j) in zip(days,tem_c)})


# using if condition 
products = {'phone' : 10 , 'laptop' : 0 , 'charger' :32 , 'tablet' : 0} 
print({i:j  for (i,j) in products.items() if j!=0})


#nested comprehension 

# Print tables of numbers from 2 to 4. 
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})
















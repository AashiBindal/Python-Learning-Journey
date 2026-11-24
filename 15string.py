#creating strings 
a='hello'
b="hello"
c='''hello'''
d="""hello"""
e=str('hello')
print(a , b , c , d , e)
#-------------------------------
#positive indexing
f='hello world'
print(f[0])

#negative indexing 
f='hello world'
print(f[-3])
#--------------------------------
#slicing
g='hello world' 
print(g[0:5])

g='hello world' 
print(g[6:11])

g='hello world' 
print(g[:8])

g='hello world' 
print(g[2:])

#slicing with step size
g='hello world'
print(g[0:8:2])

g='hello world'
print(g[6:0:-2])

#reverse string
g='hello world'
print(g[::-1])

g='hello world'
print(g[-6:])

g='hello world'
print(g[-1:-6:-1])
#----------------------------------
#python strings are immutable
#h='hello'
#del h
#print(h)
#---------------------------------
#operations on string 

#1 arthemetic operator
print('hi ' + 'aashi ' +'!')
print('DELHI '*5)
print("*"*30)

#2 relational operator
print('Delhi'== 'delhi') #case sensitive
print('pune' !='mumbai ')
print('mumbai'>'pune') # lexiographically
print('ashi' >'aashi')
print('mumbai'>'Mumbai')

#3 logical operator
print("hello" and "world")
print("hello" or "world")
print(not '')
print(not'hello')

#4 loops on string
for i in 'hello':
    print(i)

for i in 'delhi':
    print('pune')

#5 membership operator
print('D' in 'Delhi')
print('d' in 'Delhi') 
print('d' not in 'Delhi')

#-------------------------------------

# common Functions 
#len -> count length of string
print(len('AASHI BINDAL'))
#max -> extract the max valued string based on ascii value
print(max('hello world'))
#min -> find min value based on ascii value
print(min('hello world'))
#sorted ->sort in ascending order based on ascii value
print(sorted('adfbcAEe'))
#for descending order
print(sorted('adfbcAEe',reverse=True))

#----------------------------------------

#capitalize ->1st letter change into capital letter
a='heLlO woRlD'
print(a.capitalize())
#Title ->change 1st letter of each word or sent into capital
print(a.title())
#Upper ->change all char into upper
print(a.upper())
#Lower -> change all char itno lower
print(a.lower())
#Swapcase -> change cap into lower and viceversa
print(a.swapcase())

#------------------------------------------

#count->find no. of char present in string
b='my name is aashi'
print(b.count('i'))
#find -> find the index of char
print(b.find('is'))
print(b.find('z'))
#index -> find the index of char but if some char is not find show error

#--------------------------------------------
b='my name is aashi'
#endswith ->check end chars
print(b.endswith('hi'))
#startswith -> check start char
print(b.startswith('my'))

#---------------------------------------------

#format
n = input('enter name : ')
g = input('enter gender: ')
print('hi my name is {} and i am a {}'.format(n,g))

#-----------------------------------------------

#isalnum -> check alpha numeric string
c = 'ashi1234'
print(c.isalnum())
c='ashi1234@5'
print(c.isalnum())
#isalpha -> check every char is a alphabet or not
c='aashi'
print(c.isalpha())
c='aashi123'
print(c.isalpha())
#isdigit -> check digit
c='123'
print(c.isdigit())
#isidentifier -> check valid or nonvalid identifier

#------------------------------------------------------

#split() -> split sen into list 
a='my name is ashi'
print(a.split())
print(a.split('a'))
#join()  -> reverse of split
a='my' ,'name' , 'is' , 'ashi'
print('-'.join(a))

#-------------------------------------------------------

#replace
'hi my name is aashii'.replace('aashii','AASHI')

#strip
a = 'aashi                   '
print(a.strip())
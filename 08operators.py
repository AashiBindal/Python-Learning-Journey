# operators are used to perform operations on variables and value. python has the following operators 
# arithmetic operators 
# comparison operators 
# logical operators 
# bitwise opperators
# assgnment operators 
# identity operators 
# membership operators 

x=5
y=2
print('arthimetic operator')
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//2) #quotient convert into integer 
print(x%y)
print(x ** y) # for power 

print('comparision operator') #relational operator
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x==y)
print(x!=y)

print('logical operators')
q = True
r = False 

print(q or r)
print(q and r)
print(  not r)
print(  not q)

print( 'bitwise operator')
x = 2          #2 = 010
y = 3          #3 = 110
print(x & y )    #= 010=2
print(x | y )
print(x >> 2 )
print(y << 3)
print(~ x)
print(x ^ y) #xor

print('assgnment operator')
f = 4
print(f)

f += 5 
print(f)

f *=3
print(f)

print('identity operator')

g=5
h=5

print(g is h )

j="hello"
l="hello"
print(j is l)

a=[1,2,3,4]
b=[1,2,3,4]
print(a is b)

o="Hello-world"
p="Helloworld"
print(o is p )
print(o is not p)

print(" membership operators ")

u="bkjfyua aoibujbaf bvay"
print("i" in u )
print("i" not in u )

k=[1,2,3,4,5,5,6,7,8,8,9,0]
print(9 in k )

# find the sum of a 3 digit no. entered by the user 
number = int(input('enter 3 digit no. :  '))
a = number % 10 
number = number//10 
b=number% 10 
number = number//10
c=number%10     
number = number//10
print(f"sum of 3 digit no. is {a+b+c}")
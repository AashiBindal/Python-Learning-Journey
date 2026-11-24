# 1/1! +2/2! + 3/3! ....
n = int(input('enter n : '))
result = 0 
fact = 1 
for i in range(1 , n+1):
    fact=fact*i
    result = result +i/fact
print(result)

import math
print('factorial of 5 is : ',math.factorial(5))

#NESTED LOOP
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

#print pattern 
#1 
rows = int(input('enter no. of rows : '))
for i in range(1 , rows+1):
    for j in range(1 , i+1):
        print('*' , end=' ')
    print()  
#2
n = int(input('enter no. : '))
for i in range(1 , n+1):
    for j in range(1, n+1):
        print("*", end=' ' )
    print()    
#3 solid rectangle 
n=int(input('enter no. : '))
for i in range(1 , n+1):
    for j in range(1 , 6):
        print("*", end=' ' )
    print()
#4     
n=int(input('enter no. of rows : '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j , end=' ')
    for k in range(i-1,0,-1):
        print(k , end=' ')    
    print()    
    
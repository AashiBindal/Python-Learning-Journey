#1
n=int(input('enter no. of rows : '))
for i in range(1,n+1):
    for j in range(i ,0 , -1):
        print(j , end=' ')
    print()    
#2
n=int(input('enter no. of rows :'))
for i in range(n, 0 , -1 ):
    for j in range( 1 ,i+1 ):
        print(j , end=" ")
    print()
#3
n=int(input('enter no. of rows : '))   
for i in range( 1, n+1):
    for j in range(n , i-1 , -1):
        print(j , end=' ')
    print() 
#4
n=int(input('enter no. of rows : '))
for i in range(n , 0 , -1):
    for j in range(i , 0 , -1):
        print(j , end=' ')  
    print()    
#5
n=int(input("enter no. of rows : "))
for i in range(1 , n+1 ):
    for j in range(1 , i+1 ):
        print(j , end=' ' )
    print()    
for i in range(n-1 ,0 , -1):
    for j in range(1 , i+1):    
        print(j , end=' ')    
    print()  
#6
n=int(input('enter no. of rows : '))   
for i in range(n , 0 , -1):
    for j in range(n , i-1 , -1):
        print(j , end=" ")
    print()
for i in range(1, n):
    for j in range(n, i, -1):
        print(j, end=" ")
    print()        
#7
n=int(input('enter no. of rows : '))  
num=1 
for i in range(1 ,n+1):
    for j in range(i):
        print(num , end=" ")
        num+=1
    print()    
#8
n = int(input('enter no. : '))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#9    
n=int(input("enter number: "))
for i in range(1 , n+1):
    for j in range(1 , n+1):
        if i%2!=0 or j%2==0:
            print("0" , end=' ')
        else : print("1" , end=' ')    
    print( )    
#10
n = int(input("Enter no. of rows: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()    
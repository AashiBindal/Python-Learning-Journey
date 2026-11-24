#while
number = int(input('enter the number  :  '))
i=1 

while i<11 :
 print(number , '*' , i,'=' , number*i)
 i+=1 

print('while loop with else ')
x =1 

while x < 3 :
    print(x)
    x+=1 

else : 
  print('limit crossed ')    

print('guess the number game ')
import random
jackpot = random.randint(1,100)

guess=int(input('guess the number btw 1 to 100 : '))  
counter = 1
while guess != jackpot :
  if guess < jackpot :
    print('guess higher ..')
  else :
    print('guess lower..')

  guess = int(input('again guess : '))
  counter +=1 

else:
  print('correct guess !!')    
  print('attempts made : ',counter)

#for loop 

print('for loop ')
for i in range(1, 11):
  print(i)

print('print city name ')
for i in 'INDORE':
    print(i)

print('Program: The current population of a town is 10,000.' \
' The population of the town is increasing at the rate of 10% per year.' \
' You have to write a program to find out the population at the end of each of the last 10 years.')    
cur_pop = 10000

for i in range(1,11,-1):
  print(i , cur_pop)
  cur_pop = cur_pop/1.1
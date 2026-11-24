# find the length of a given string without using len() function
s = input('enter the string : ')
counter = 0
for i in s:
    counter+=1

print('length of string is : ' , counter)    

#extract username from a given email
# eg if mail is aashibindal@gmail.com
# then the username should be aashibindal

s = input('enter the mailId : ')

pos = s.find('@')
print(s[0:pos])

#count the frequency of a particular char in a provided string

s = input('enter the string : ')
term = input('char search : ')
#print(s.count(term))
counter = 0

for i in s:
    if i==term:
        counter+=1

print('frequency : ' , counter)      

#write a program which can remove a particular char from a string

s = input('enter the string : ')
term = input('what would like to remove: ')

result =''
for i in s:
    if term!=i:
        result=result+i

print(result)

#write a program that can check wheather a given string is palindrome or not 
#malayalam
s = input('enter the string : ')
for i in range(0,len(s)//2):
    if s[i] != s[len(s)-i-1]:
        print("not palindrome !")
        break 
else:
    print("palindrome!!")

#write a program to count the no. of words in a string without split() 
s = input('enter the string : ')
count = 0 
for i in range(len(s)):
    if s[i] ==' ':
        count+=1
print('number of words : ' , count+1 )       

#write a python program to convert a string to title case without using the title()
s = input('enter the string : ')

L=[]
for i in s.split():
   L.append(i[0].upper() + i[1:].lower())

print(" ".join(L))

#write a program that can convert an integer to string 
number = int(input('enter the integer : '))
digits = '0123456789'
result = ''
while number != 0:
    result = digits[number % 10] + result 
    number = number//10

print(result)    
print(type(result))

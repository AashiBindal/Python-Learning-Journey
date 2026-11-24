# login program and intentation 

#email->aashibindal296@gmail.com
#password->1234

email= input('enter you mail id :  ')
password = input('enter your password :  ')

if email == 'aashibindal296@gmail.com' and password =='1234' :
   print('login succesfull !! ')
elif email == 'aashibindal296@gmail.com' and password != '1234':
   print('inccorect password !!')
   password = input('enter your password again !!')
   #nested if else 
   if password =='1234' :
      print("login successfull !! ")  
   else :
      print('login failed !! ')
else : 
   print('login failed !! ')   

#find the min of 3 given number 
a= int(input('enter 1st no. :  '))
b= int(input('enter 2nd no. :  '))
c= int(input('enter 3rd no. :  '))
if a<b and a<c :
   print('smallest no. is : ' , a)
elif  b<c :
   print('smallest no. is : ' , b)
else :
   print ('smallest no. is : ' , c)   

#menu driven calculator 

fnum = int(input('enter first no. :  '))
snum = int(input('enter second no. :  '))

op = input('enter the operation : ')

if op =='+' :
   print(f"sum of {fnum} + {snum} is : " , fnum + snum)

elif op =='-' :
   print(f"subtraction of {fnum} - {snum} is : " , fnum - snum)   

elif op =='*' :
   print(f"multiplication of {fnum} * {snum} is : " , fnum * snum)
else : 
   print(f"division of {fnum} / {snum} is : " , fnum / snum)         

   
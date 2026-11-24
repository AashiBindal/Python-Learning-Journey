 # input()

input(  "whats your name  :  ")

input( "age : ")

#take input from the user and store them in a variable 
fnum = input('Enter 1st no. :  ')
snum = input('Enter second no. : ')
print(fnum , snum)
# add the 2 variables 
# result = fnum + snum gives the output as 1234 if user enter 12 and 34 because python store the input in string format
result = int(fnum) + int(snum)
#print the result
print(result)
print(type(fnum)) # still the datatype of fnum is string because we have converted it into int in the result variable only not in fnum variable

# typeconversion se actual value convert nai hoti hai , ek duplicate variable me convert hoti hai , original variable ka datatype change nai hota hai
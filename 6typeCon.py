first_num = input("enter the first number: ")
second_num = input("enter the second number: ")
print(first_num + second_num )
# python user input ke output ko string me store krta hai thats why ye yha p numerically add nhii ho paa rhe hai
# now ye problem solve hogi type conversion se 

#type (it is a function jo btyga ki kya datatype hai )

# type conversion 
#convert one data type into another 
# there are 2 type conv
# implicit
# explicit

print(4 + 7.8) #implicit (python khud se convert krra hai )
print(4.5 + 5+5j)  # implicit 

#explicit
print("addition of two numbers:")
result = int(first_num) + int(second_num)
print(result)

a = int(input("enter the 1st  no. : "))
b = int(input("enter the 1st  no. : "))
result = a+b
print(result)

#str->int
print(type(int('5')))

#complex->int
print(type(int(5+3j))) # error because complex number cannot be converted into int
# literals is a raw data given in a variable 
# numeric 
# string 
# boolean
# special 

#numeric litreal 
a = 0b1010 #binary literals 
b = 100    #decimal literals
c = 0o310  # octal literals
d = 0x12c  # hexadecimal literals
print(a,b,c,d)

#float literals
float_1 = 10.5
float_2 = 1.5e2 # 1.5 10 raise to power 2 
float_3 = 1.5e-3
print(float_1,float_2,float_3)

#complex literals
x = 3.14j # without writing real part (i)
print(x,x.imag , x.real)

#string literals 
string = "this is string"
strings = 'this is also a string'
char = "c" # no need in pyhton , python suppossed char as a string
multiline_str = """this is a multiline string with more than one line code"""
unicode = u"\U0001f600\U0001f606"
raw_str = r"raw \n string "

print(string,strings,char,multiline_str,unicode,raw_str)

#boolean literals
a = True + 10
b = False + 10
print("a:" ,a )
print("b:" , b)

#special literals
a = None 
print(a)

x=None 
y = 5 
z= 6 
print('program exe')
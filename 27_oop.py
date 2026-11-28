# oop gives a programmmer the power to create its own data type !!
# Principle of OOP:
#- class :- blueprint ( a set of rules how object behaves)
# --data or property & functions or behavior
#- object :- object is an instance of the class 
#- inheritance
#- polymorphism
#- abstraction
#- encapsulation

#class basic structure 
class car :
    colour ='blue' #data
    model = 'sports' # data
    def calculate_avg_speed(km,time):
        print()#some code 

#class name always in pascal case (HelloWorld)

#syntax to create an object
#objectname = classname()     

#always create variable inside the constructor
# and use self.


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



class Atm :
    # constructor -> no need to call explecitly , it runs automatically when object is created !!
    # self is use for interclass communication 
    def __init__(self):
        self.pin ='' 
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
            hi how can I help you ?
            1.press 1 to create pin
            2.press 2 to change pin
            3.press 3 to check balance
            4.press 4 to withdraw
            5.exit
        """
            )

        if user_input == '1':
            self.create()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
             self.check_balance()
        elif user_input == '4':
              self.withdrawl()
        else :
              exit()

    def create(self):
        user_pin = input('enter your pin :  ')
        self.pin = user_pin 

        user_balance = int(input('enter your balance :  '))
        self.balance = user_balance

        print('pin created sucessfully !!')
        self.menu()

    def change_pin(self):
        old_pin =  input('enter your old pin : ')  

        if old_pin == self.pin :
              # let him/her change the pin
              new_pin = input('enter your new pin :  ')
              self.pin = new_pin
              print("pin change successful !!")
              self.menu()
        else :
              print("enter correct pin !! ")      
              self.menu()


    def check_balance(self):
          user_pin = input('enter your pin : ')
          if self.pin == user_pin :
                print('your balance is ' , self.balance)
          else :
                print('enter correct pin !! ')   
          self.menu()


    def withdrawl(self) : 
         user_pin = input('enter pin : ')
         if self.pin == user_pin :
              amount = int(input('enter the amount : '))
              if  0< amount <= self.balance:
                   self.balance = self.balance - amount 
                   print('withdrawl successful ! \n balance is ' ,self.balance)
                   self.menu()
              else :
                   print("invalid amount or insufficient balance! ")    
                   self.menu()
        

obj = Atm()


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


# functions vs method 

#- Function: A function is an independent, reusable block of code that performs a specific task. It is defined outside a class.
#- Method: A method is a function defined inside a class and is generally used to perform operations related to its objects.

l = [1,2,3]
len(l) # function -> bcos it is outside the list class
l.append() # method -> bcos it is inside the list class



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


# fraction datatype 

class Fraction :
     #parameterized constructor 
     def __init__(self,x,y):
          self.num = x
          self.den = y

     def __str__(self):
          return  '{}/{}'.format(self.num , self.den)

     def __add__(self , other ):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den

        return  '{}/{}'.format(new_num , new_den)
     

     def __sub__(self,other):
       new_num = self.num*other.den - other.num*self.den
       new_den = self.den*other.den
     
       return  '{}/{}'.format(new_num , new_den)
     

     def __mul__(self,other):
       new_num = self.num*other.num
       new_den = self.den*other.den
     
       return  '{}/{}'.format(new_num , new_den) 


     def __truediv__(self,other):
       new_num = self.num*other.den 
       new_den = self.den*other.num
     
       return  '{}/{}'.format(new_num , new_den)

     def convert_to_decimal(self):
      return self.num/self.den
     
fr1 = Fraction(8,4)
fr2 = Fraction(1,2)
print(fr1)
print(fr2)          
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1.convert_to_decimal())



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------





















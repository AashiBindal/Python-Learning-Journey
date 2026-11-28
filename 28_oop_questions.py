#Q-1: Rectangle Class
#Write a Rectangle class in Python language, 
#allowing you to build a rectangle with length
#and width attributes.

#Create a Perimeter() method to calculate the
#perimeter of the rectangle and a Area() method to
#calculate the area of ​​the rectangle.

#Create a method display() that display the length, width,
#perimeter and area of an object created using an instantiation
#on rectangle class.

class Rentangle:

    def __init__(self,length , width):
        self.length =  length 
        self.width =  width

    def perimeter(self) :
        return 2*(self.length+self.width)

    def Area(self):
        return self.length*self.width 

    def Display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.perimeter())
        print("Area:", self.Area())

length = float(input(" enter the value of length : "))    
width =  float(input(" enter the value of width : "))    
    
obj = Rentangle(length,width)

obj.Display()


#Q-2: Bank Class
#Create a Python class called BankAccount which
#represents a bank account,
#having as attributes: accountNumber (numeric type),
#name (name of the account owner as string type), balance.

#Create a constructor with parameters: accountNumber, name, balance.

#Create a Deposit() method which manages the deposit actions.

#Create a Withdrawal() method which manages withdrawals actions.

#Create an bankFees() method to apply the bank fees with a percentage 
# of 5% of the balance account.

#Create a display() method to display account details. Give the
#complete code for the BankAccount class.


class BankAccount :

    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name       = name   
        self.balance    = balance

    def Deposit(self):
        self.deposit = int(input('enter amount for deposite : '))
        self.balance = self.deposit + self.balance  
        return self.balance 


    def Withdrawl(self):
         self.withdrawl = int(input('enter amount for withdrawl  : '))
         if 0 < self.withdrawl <= self.balance :
           self.balance = self.balance - self.withdrawl 
           return self.balance
         
         else :
             print("insufficient balance !!") 
    
    
    def BankFees(self):
        self.Bankfees = self.balance*0.05
        self.balance = self.balance - self.Bankfees
        return self.balance
    

    def Display(self):
         print('your account number : ' , self.accountNumber)    
         print('your name : ' , self.name)
         print('total balance : ' ,self.balance)

accountNumber = int(input('enter your account number : '))    
name          = input('enter your name : ')
balance       = int(input('enter balance : '))


obj = BankAccount(accountNumber,name,balance)
obj.Display()

obj.Deposit()
obj.Display()

obj.Withdrawl()
obj.Display()

obj.BankFees()
obj.Display()
























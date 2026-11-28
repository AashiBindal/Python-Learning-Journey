class BankAccount :

    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name       = name   
        self.balance    = balance

    def Deposit(self):
        self.deposit = int(input('enter amount : '))
        self.balance = self.deposit + self.balance  
        return self.balance 


    def Withdrawl(self):
         self.withdrawl = int(input('enter amount : '))
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


"""Create a bank account class that has attributes owner, balance 
and two methods deposit and withdraw. Withdrawals may not 
exceed the available balance. Instantiate your class, 
make several deposits and withdrawals, and test to make 
sure the account can't be overdrawn."""

class BankAccount:
    def __init__(self, name):
        self.owner=name
        self.balance=0
    def deposit(self, x):
        self.balance+=x
        print("Current balance:{}$".format(self.balance))
    def withdraw(self,x):
        if(x>self.balance):
            print("{}, you have no enough balance for the withdrawal!".format(self.owner))
        else:
            self.balance-=x
            print("{}$ withdrawed succesfully".format(x))
            print("Current balance:{}$".format(self.balance))

acc=BankAccount("uldana")
acc.deposit(1000)
acc.withdraw(1500)
acc.deposit(600)
acc.withdraw(1000)
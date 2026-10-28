class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance,interest_rate):
        self.interest_rate = interest_rate
        super().__init__(owner, balance)  
    def add_interest(self):
        self.deposit(self.balance * self.interest_rate)
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance,overdraft_limit):
        self.overdraft_limit = overdraft_limit
        super().__init__(owner, balance)
    def withdraw(self,amount):
            if amount <= self.overdraft_limit:
                self.BankAccount__balance -= amount
            else:
                print("Overdraft limit exceeded!")
#Test
acc1 = BankAccount("Ali", 1000)
acc2 = SavingsAccount("Reza",2000,0.005)
acc1.deposit(500)
acc1.withdraw(2000)
acc2.add_interest()
print(acc1.balance)
print(acc2.balance)
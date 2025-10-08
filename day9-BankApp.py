# create class

# v = 520
#string formats
#1. raw string
#2. formatted string
#3. bytes



#parent class
class BankAccount:
    #constructor
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        # return self.balance
        return f"Deposited amount of ${amount}. New Balance is {self.balance} "
    
    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            # return self.balance
            return f"Withdraw amount of ${amount}. Remaining Balance is ${self.balance}"
        else:
            return "Insufficient balance"
        
    def get_balance(self):
        return f"Account balance is ${self.balance}"


class SavingsAccount(BankAccount):
    #creating constructor
    def __init__(self, account_number, holder_name, balance=0, interest_rate = 0.3):
        #inheriting parent class constructor
        # super() - refers to parent class
        super().__init__(account_number,holder_name,balance)
        self.interst_rate = interest_rate   

    def add_interest(self):
        interest = self.balance * self.interst_rate
        self.balance += interest
        return f"Interest add ${interest:3f}. New balance is ${self.balance:3f}"
    


class CheckingBalance(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=500):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            print(self.balance)
            print(amount)
            self.balance -= amount
            return f"Withdraw amount of ${amount}. Remaining Balance is ${self.balance}"
        else:
            return "Insufficient balance, overdraft limit exceeded"
        
account = [SavingsAccount("SA1001","John",0),
CheckingBalance("SA1001","Raj",500)]

for a in account:
    print(a.withdraw(600))




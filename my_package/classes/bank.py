class BankAccount:
    #def__init__(self):
	    #print(“Default Constructor”)

    def __init__(self, account_holder, balance=0):	
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance}")

account1 = BankAccount("Nithya", 1000)
account1.deposit(1000)
account1.withdraw(300)
account1.check_balance()
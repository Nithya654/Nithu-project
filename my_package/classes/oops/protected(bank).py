class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Deposited:", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self._balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Account Holder:", self.holder)
        print("Current Balance:", self._balance)


account1 = BankAccount("Nithya", 5000)
account1.deposit(1000)
account1.withdraw(1500)
account1.check_balance()

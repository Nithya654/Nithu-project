balance = 3000

def create_account():
    print("Account successfully created!")
    balance=3000
    print("Your current balance is", balance)

def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance =balance + amount
    print("Deposited", amount, ". Your new balance is", balance)

def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance =balance - amount
        print("Withdraw", amount, ". Your new balance is", balance)
    else:
        print("Insufficient balance!")

def check_balance():
    print("Your current balance is", balance)

def banking():
    while True:
        print("\n--- Banking Application ---")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")

        choice = int(input("Please select an option (1-5):"))
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            print("Exiting the application. Thank you for using our service!")
            break
        else:
            print("Invalid choice. Please choose a valid option between 1 to 5.")
banking()

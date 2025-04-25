# Global user data
user_data = {
    "1234": {
        "name": "Vishwa",
        "balance": 5000
    }
}
# --- Functions --
def welcome():
    print("\n=== Welcome to Python ATM ===")

def authenticate():
    pin = input("Enter your 4-digit PIN: ")
    if pin in user_data:
        print(f"Welcome, {user_data[pin]['name']}!")
        return pin
    else:
        print("Invalid PIN.")
        return None

def show_balance(pin):
    print(f"Current Balance: ₹{user_data[pin]['balance']}")

def deposit(pin):
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        user_data[pin]['balance'] += amount
        print(f"₹{amount} deposited successfully.")
    else:
        print("Invalid amount.")
    show_balance(pin)

def withdraw(pin):
    amount = float(input("Enter amount to withdraw: ₹"))
    if 0 < amount <= user_data[pin]['balance']:
        user_data[pin]['balance'] -= amount
        print(f"₹{amount} withdrawn successfully.")
    else:
        print("Insufficient balance or invalid amount.")
    show_balance(pin)

def main_menu(pin):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_balance(pin)
        elif choice == "2":
            deposit(pin)
        elif choice == "3":
            withdraw(pin)
        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# --- Main Program ---
welcome()
user_pin = authenticate()
if user_pin:
    main_menu(user_pin)



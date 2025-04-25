"""
Project 4:Create a Mini Monthly/Yearly Expense Tracker 
using library Math, Date Time Function, 
Function, List,Tuple and Dictionary

Provide the Output..Create Your own functions
"""
import math
import datetime

#1:Store expenses in a list of dictionaries
expenses = {}

#2:Function to add an expense
def add_expense(amount, category, date):
    expense = {
        "amount": amount,
        "category": category,
        "date": date  
    }
    expenses.append(expense)
    print(f"Added ₹{amount} for '{category}' on {date.strftime('%Y-%m-%d')}.")

#3:to view total monthly expenses
def monthly_expense_report(month, year):
    total = 0
    for exp in expenses:
        if exp["date"].month == month and exp["date"].year == year:
            total += exp["amount"]
    print(f"Total expenses for {month}/{year}: ₹{total}")

#4:to view total yearly expenses
def yearly_expense_report(year):
    total = 0
    for exp in expenses:
        if exp["date"].year == year:
            total += exp["amount"]
    print(f"Total expenses for {year}: ₹{total}")

#5:to show all expenses
def show_all_expenses():
    print("\n All Expenses:")
    for exp in expenses:
        print(f"₹{exp['amount']} - {exp['category']} on {exp['date'].strftime('%Y-%m-%d')}")

#6:Menu to display
def main_menu():
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Monthly Expense")
        print("3. View Yearly Expense")
        print("4. Show All Expenses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount (₹): "))
                category = input("Enter category (e.g., food, rent, travel): ")
                date_input = input("Enter date (YYYY-MM-DD): ")
                date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d")
                add_expense(amount, category, date_obj)
            except Exception as e:
                print("Invalid input:", e)
        elif choice == "2":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2025): "))
            monthly_expense_report(month, year)
        elif choice == "3":
            year = int(input("Enter year: "))
            yearly_expense_report(year)
        elif choice == "4":
            show_all_expenses()
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1-5.")

main_menu()

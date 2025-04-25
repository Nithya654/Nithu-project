import math
def split_bill():
    people = []
    total = 0
    print("Welcome to the Simple Bill Splitter!")
    num_people = int(input("Enter the number of people: "))

    # Get names of all people
    for i in range(num_people):
        name = input("Enter name of person " + str(i+1) + ": ")
        people.append(name)
    print("")
    print("Now, enter each person's spending.")
    print("")

    # Store each person's spending
    expenses = []
    for person in people:
        amount = float(input("Enter amount spent by " + person + ": "))
        expenses.append(amount)
        total += amount

    # Calculate equal share using lambda
    equal_share = (lambda total, count: round(total / count, 2))(total,num_people)
    print("")
    print("----- Bill  -----")
    print("Total Spent: ₹", round(total, 2))
    print("Each person should pay: ₹", equal_share)
    print("")

    print("----- Balance Sheet -----")
    for i in range(num_people):
        balance = round(expenses[i] - equal_share, 2)
        if balance > 0:
            print(people[i], "should receive ₹", balance)
        elif balance < 0:
            print(people[i], "should pay ₹", abs(balance))
        else:
            print(people[i], "is settled up")

    print("")
    print("Thank you for using the Bill Splitter!")

split_bill()

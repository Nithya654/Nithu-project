#First Example:Basic try-except

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")

#Second Example: Multiple Try Except

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#Third: else and finally blocks

try:
    print("Trying something...")
    x = 1 / 1
except ZeroDivisionError:
    print("Oops, division by zero.")
else:
    print("No errors occurred!")
finally:
    print("This always runs.")


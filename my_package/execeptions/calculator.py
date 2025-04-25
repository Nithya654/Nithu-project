#Simple Calculator Program:

def simple_calculator():
    print("Welcome to the Simple Calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operation!")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except Exception as e:
        print(f"Something went wrong: {e}")

# Run the calculator
simple_calculator()

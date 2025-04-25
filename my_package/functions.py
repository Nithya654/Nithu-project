import math
import string
# 1. Simple function
def greet():
    """Function to greet the user."""
    print("Hello welcome to Hexaware!")

# 2. Function with parameters
def greet_person(name):
    """Function to greet a person with their name."""
    print(f"Hello, {name}!")

# 3. Function with return value
def add(a, b):
    """Function to add two numbers."""
    return a + b

# 4. Default parameters
def greet_default(name="Guest"):
    """Function to greet a person with a default name."""
    print(f"Hello, {name}!")

# 5. Function with multiple return values
def math_operations(a, b):
    """Function that returns multiple math results."""
    return a + b, a - b, a * b, a / b

# 6. Lambda function
multiply = lambda x, y: x * y

# 7. Variable arguments (*args)
def print_numbers(*args):
    """Function to print a variable number of arguments."""
    for num in args:
        print(num)

# 8. Variable keyword arguments (**kwargs)
def print_student_info(**kwargs):
    """Function to print student information."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 9. Recursive function to calculate factorial
def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# 10. Docstring function example (using help())
def example_function():
    """This is an example function with a docstring."""
    return "This function demonstrates docstrings!"

#calling all fn
#1 greeting msg
greet()

#2 1 arg name
greet_person("Nithya")

#3 to sum
sum_result = add(10, 5)
print(f"Sum: {sum_result}")

#4 default value
greet_default()
greet_default("Aditya")

#5.multiple val
sum_val, diff_val, prod_val, quot_val = math_operations(10, 2)
print(f"Sum: {sum_val}, Difference: {diff_val}, Product: {prod_val}, Quotient: {quot_val}")

#6.lambda/anonymous fn
result = multiply(3, 4)
print(f"Lambda multiplication result: {result}")

# 7. Variable arguments
print("Printing variable arguments:")
print_numbers(1, 2, 3, 4, 5)

# 8. Variable keyword arguments
print("Printing student info:")
print_student_info(name="Niruba", age=21, course="Python")

# 9. Recursive function
factorial_result = factorial(5)
print(f"Factorial of 5: {factorial_result}")

# 10.Displaying the docstring of the function using help()
print("Displaying docstring of example_function:")
help(example_function)


def initialize_tuple():
    return ("apple", "banana", "cherry")

fruits = initialize_tuple()
print("Initialized Tuple:", fruits)

#all in one
def initialize_all():
    my_list = [1, 2, 3]
    my_tuple = ('a', 'b', 'c')
    my_dict = {'key': 'value'}
    my_set = {100, 200, 300}
    return my_list, my_tuple, my_dict, my_set


lst, tpl, dct, st = initialize_all()
print("List:", lst)
print("Tuple:", tpl)
print("Dictionary:", dct)
print("Set:", st)

#deque
from collections import deque

def initialize_queue():
    """Initializes an empty queue."""
    return deque()

# Calling the function
queue = initialize_queue()
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)  
# Dequeuing elements
queue.popleft()  
print(queue) 

#initializing list

def initialize_list():
    return [1, 2, 3, 4, 5]

my_list = initialize_list()
print("Initialized List:", my_list)

#dict
def create_student():
    student = {
        "name": "Vishwa",
        "age": 10,
        "grade": "5th"
    }
    return student
s = create_student()
print("Student Dictionary:", s)

#map,reduce.filter

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", sum_all)



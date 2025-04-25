# # 1. SyntaxError
# # Occurs when Python code is not written correctly.

# # Example
# if True
#     print("Hello")  # Missing colon causes SyntaxError

# # 2. NameError
# # Happens when you try to use a variable that hasn't been defined.

# # Example
# print(x)  # x is not defined


# 3. TypeError
# Occurs when you try to use the wrong data type for an operation.

# print("5" + 5)  # Can't add string and integer


# 4. ValueError
# Raised when a function receives an argument of the right type but inappropriate value.

# int("abc")  # Can't convert string to integer


# 5. IndexError

# nums = [1, 2, 3]
# print(nums[5])  # Index out of range


# 🔹 6. KeyError
# Raised when a dictionary key is not found.

# data = {"name": "Alice"}
# print(data["age"])  # 'age' key doesn't exist


# 🔹 7. AttributeError
# Raised when an invalid attribute is accessed for an object.

# x = 5
# x.append(3)  # int has no 'append' method


# 🔹 8. ZeroDivisionError

# 10 / 0  # Can't divide by zero


# 🔹 9. FileNotFoundError
# Raised when trying to open a file that doesn't exist.

# with open("notfound.txt", "r") as f:
#     content = f.read()


# 🔹 10. ImportError / ModuleNotFoundError
# When importing a module that doesn't exist or can't be loaded.

# import nonexistingmodule


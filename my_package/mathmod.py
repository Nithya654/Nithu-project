import math

#1.Square Root
number = 16
sqrt_result = math.sqrt(number)
print(f"Square root of {number}: {sqrt_result}")

# 2. Factorial
factorial_num = 5
factorial_result = math.factorial(factorial_num)
print(f"Factorial of {factorial_num}: {factorial_result}")

# 3. Power (Exponentiation)
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent}: {power_result}")

# 4. Logarithm (Natural Logarithm)
log_result = math.log(10)
print(f"Natural logarithm of 10: {log_result}")

# 5. Trigonometric Functions (sin, cos, tan)
angle_deg = 30
angle_rad = math.radians(angle_deg)  # Convert angle to radians
sin_result = math.sin(angle_rad)
cos_result = math.cos(angle_rad)
tan_result = math.tan(angle_rad)
print(f"Sine of {angle_deg}°: {sin_result}")
print(f"Cosine of {angle_deg}°: {cos_result}")
print(f"Tangent of {angle_deg}°: {tan_result}")

# 6. Rounding Functions
round_result = round(3.14159, 2)
ceil_result = math.ceil(3.1)
floor_result = math.floor(3.9)
print(f"Rounded value of 3.14159 to 2 decimal places: {round_result}")
print(f"Ceiling of 3.1: {ceil_result}")
print(f"Floor of 3.9: {floor_result}")

# 7. Greatest Common Divisor (GCD)
gcd_result = math.gcd(36, 60)
print(f"GCD of 36 and 60: {gcd_result}")

# 8. Degrees and Radians Conversion
degrees = 90
radians = math.radians(degrees)
converted_degrees = math.degrees(radians)
print(f"{degrees} degrees in radians: {radians}")
print(f"{radians} radians in degrees: {converted_degrees}")

# 9. Hypotenuse (Pythagorean Theorem)
side1 = 3
side2 = 4
hypotenuse_result = math.hypot(side1, side2)
print(f"Hypotenuse of a right triangle with sides {side1} and {side2}: {hypotenuse_result}")

# 10. Math Constants (Pi and e)
print(f"Value of Pi: {math.pi}")
print(f"Value of Euler's number (e): {math.e}")


print("===math functions and examples===")

#1.positive float number
number1 = 3.1
ceil_result1 = math.ceil(number1)
print(f"The ceiling of {number1} is: {ceil_result1}")

# 2. Example with a negative float number
number2 = -2.7
ceil_result2 = math.ceil(number2)
print(f"The ceiling of {number2} is: {ceil_result2}")


# 3. Example with a whole number (no change)
number3 = 5.0
ceil_result3 = math.ceil(number3)
print(f"The ceiling of {number3} is: {ceil_result3}")

# 4. Example with a large float number
number4 = 100.65
ceil_result4 = math.ceil(number4)
print(f"The ceiling of {number4} is: {ceil_result4}")

# 5. Using ceil with a calculation result
number5 = math.sqrt(16)  # Square root of 16 is 4.0
ceil_result5 = math.ceil(number5)
print(f"The ceiling of the square root of 16 ({number5}) is: {ceil_result5}")

#using floor
import math

#Using math.floor() with a positive number
positive_number = 5.7
floor_value_positive = math.floor(positive_number)
print(f"The floor value of {positive_number} is {floor_value_positive}")

# Using math.floor() with a negative number
negative_number = -3.4
floor_value_negative = math.floor(negative_number)
print(f"The floor value of {negative_number} is {floor_value_negative}")

# Using math.floor() with zero
zero_number = 0.0
floor_value_zero = math.floor(zero_number)
print(f"The floor value of {zero_number} is {floor_value_zero}")







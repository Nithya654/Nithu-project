x=12
if x%3==0:
    print("x is divisible by 3")
else:
    print("x is not divisible by 3")

x=11
if x%3==0:
    print("x is divisible by 3")
elif x%5==0:
    print("x is divisible by 5")
else:
    print("x is not divisible by 3 or 5")

#prime or not
a = 3
if a>1:
    for x in range(2,a):
        if (a%x)==0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("value of a  is >=1")

x=19
y=10
print(type(x),type(y))

r=45.6
print(type(r))

s=10+6j
print(type(s))

v=2>6
print(type(v))
print(v)

my_string ="this is python"
print(my_string)

a=5
b=7
if a<b:
    print("a is less than b")

print("a is less than b") if a<b else print("a is greater than b")

a=[1,2,3,4,5]
while a:
    print(a.pop(-1))
    b=["********"]
    while b:
        print(b.pop())

#fibonaci series
def fibonacci(n):
    fib_series =[0,1]
    for i in range(2,n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series[:n]
n=10
print(fibonacci(n))

#fibonacci generator
def fibonacci_generator():
    a,b =0,1
    while True:
        yield a
        a,b = b, a+b
n=10
fib_gen = fibonacci_generator()
fib_series = [next(fib_gen) for _ in range(n)]
print(fib_series)

#using seperator
print("Hello","python",sep = "_",end ="------------")
print("Hello Python Learning")

################################################
#assignment
#1.prime number
n = 5
if n>1:
    for i in range(2,n):
        if (n % i)==0:
            print("It is not prime")
            break
    else:
        print(" It is prime")
else:
    print("value of a is >=1 and not prime")

#2.largest of 3 num
a=10
b=15
c=5

if (a>b)and (a>c):
    print("a is the largest")
elif (b>a)and (b>c):
    print("b is greater")
else:
    print("c is greater")

#3.factorial using loop
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("Factorial of", num, "is", factorial)

#4.leap year
year = 2025
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
   
#5.reverse string using for loop
text = "Nithya sree"
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print("Original String:", text)
print("Reversed String:", reversed_text)

#6.prime number or not bw range 1 to 50
for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, "is a prime number")

#7.to print a triangle pattern
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

#8.reverse each word in sentence
sentence = "My name is Nithya"
reversed_sentence = " ".join([word[::-1] for word in sentence.split()])
print("Original Sentence:", sentence)
print("Reversed Each Word:", reversed_sentence)

#9.palingdrome or not
nums=[1,2,3,2,1]
if nums == nums[::-1]:
    print("it is a palingdrome")
else:
    print("it is not a palingdrome")

#10.simple addition using def
"""def add_numbers(num1, num2):
    return num1 + num2
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", sum_result)"""

##or
def add(a, b):
    return a + b
result = add(3, 5)
print("The sum is:", result)


#11.check odd or even
def odd_even(num):
    if num % 2 == 0:
        print("Number is",num, " it is even")
    else:
        print("Number is",num,"it is odd")
num = 12
odd_even(num)

#12.max of 2 num
def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print("Maximum is:", maximum(10, 20))

#13.def with factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact =fact*i
    return fact
num = 5
print("Factorial of", num, "is", factorial(num))

#14.count words in sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)
text = "I am Nithya"
print("Number of words:", count_words(text))

#Amstrong number or not
num=153
sum =0
temp=num
while temp>0:
    digit = temp % 10
    sum += digit **3
    temp //=10
if num == sum:
    print(num,"is an amstrong number")
else:
    print(num,"is not an amstrong number")

#using break
i=1
while i<10:
    print(i,end=" ")
    if i==5:
        break
    i=i+1
print("\n Done")

#using continue
for i in range(1,11):
    if(i==5):
        continue
    print(i,end=" ")
print("\n","done")

#slicing a string
text="HelloMyNameisNithya"
result = text[:9]
print(result)

x=text[-9:]
print(x)
#or 
for char in x:
    print(char,end="")
result=text[1:9]
print(result)

#multiplication table
n= 5
print("Multiplication table",n)
print("*************")
for i in range(1,11):
    print(n,"X",i,"=",n*i)

#to print leap year 
print("Leap year from 2015 to 2023")
for i in range(2015,2023):
   if(i%4==0):
       print(i,end=" ")
       print("\n")

#num to power with given count
num= 5
n=8
result=1
for i in range(n):
    result=result*num
    print(num,"is raised to power",n,"is",result)

#sum of cubes
n=15
s=0
for i in range(1,n+1):
   a=i**3
   s=s+a
   print(s)
print("The sum of cubes is",s)

#11.nested loops-for
for i in range(1,6):
   print("Pass",i,"-",end=" ")
   for j in range(1,6):
       print(j,end=" ")
   print()

#printing with *
for i in range(1,6):
   print()
   for j in range(i):
       print("*",end=" ")

N=5
for i in range(1,N+1):
   for k in range(N,i,-1):
       print("",end=' ')
   for j in range(1,i+1):
       print(i,end=' ')
   print()

for i in range(1,6):
   print()
   for j in range(1,i+1):
       print(j,end=' ')

#using pass
for letter in "PYTHON":
   pass
   print("Pass",letter)

#to print memory location
var1 = 10
var2 = 10

print(f"Memory location of var1: {id(var1)}")
print(f"Memory location of var2: {id(var2)}")

if id(var1) == id(var2):
    print("Both variables are using the same memory space.")
else:
    print("The variables are using different memory spaces.")

#calculate amount after simple interest
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))
simple_interest = (principal * rate_of_interest * time) / 100
total_amount = principal + simple_interest
print(f"SI is {total_amount}")








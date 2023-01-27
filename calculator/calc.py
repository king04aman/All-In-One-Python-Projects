# My first python project - An advanced calculator in Python

import math

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    return x / y

# Function to perform square root
def sqrt(x):
    return math.sqrt(x)

# Function to perform power
def power(x, y):
    return math.pow(x, y)

# Function to perform logarithm
def logarithm(x):
    return math.log(x)

# Function to perform trigonometric operations
def trig(x, operation):
    if operation == "sin":
        return math.sin(x)
    elif operation == "cos":
        return math.cos(x)
    elif operation == "tan":
        return math.tan(x)
    else:
        return "Invalid Operation"

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square Root")
print("6.Power")
print("7.Logarithm")
print("8.Trigonometry (sin, cos, tan)")

# Take input from the user
choice = input("Enter choice(1/2/3/4/5/6/7/8):")

if choice in ["1", "2", "3", "4"]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

elif choice == "5":
    num1 = float(input("Enter the number to find square root: "))
    print("Square Root of", num1, "=", sqrt(num1))

elif choice == "6":
    num1 = float(input("Enter the base number: "))
    num2 = float(input("Enter the power: "))
    print(num1, "raised to the power of", num2, "=", power(num1, num2))

elif choice == "7":
    num1 = float(input("Enter the number to find logarithm: "))
    print("Logarithm of", num1, "=", logarithm(num1))

elif choice == "8":
    num1 = float(input("Enter the angle in radians: "))
    operation = input("Enter the operation (sin, cos, tan): ")
    print(operation + "(" + str(num1) + ")", "=", trig(num1, operation))

else:
    print("Invalid Input")

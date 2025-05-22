# Operators

# 1. Arithmetic Operators: +, -, *, /, //, %, ** (addition, subtraction, multiplication, division, floor division, modulus, exponentiation)


a = input("Enter first number: ")
b = input("Enter second number: ")
try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

c= input("Enter the operator: ")


if c == "+":
    print("Addition: ", int(a) + int(b))
elif c == "-":
    print("Subtraction: ", int(a) - int(b))
elif c == "*":
    print("Multiplication: ", int(a) * int(b))
elif c == "/":
    print("Division: ", int(a) / int(b))
else:
    print("Invalid operator")
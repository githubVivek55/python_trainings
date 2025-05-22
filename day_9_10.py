# type casting
a = 4
b = int("14")

# explicit type casting
print(a+b)

c = "3.4"

# implicit type casting
# 
print(a + float(c))


# Taking input from user

a = input("Enter first number: ")

b = input("Enter second number: ")

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    print("Addition: ", a + b)
else:
    print("Invalid input. Please enter numbers only.")
    



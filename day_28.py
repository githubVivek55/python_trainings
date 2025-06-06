# f string example
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old")

# string formatting example
formatted_string = "My name is {} and I am {} years old".format(name, age)
print(formatted_string)

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))


# 0 1 1 2 3 5 8 13 21 34
def fibonacci(n):
    n0 =0
    n1 =1
    next = 0
    for i in range(2,n):
        next = n0+n1
        n0=n1
        n1=next
    return next

print(fibonacci(10))


# fibonacci series using recursion
def fibonacci_recursive(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2) 

print(fibonacci_recursive(10))

# sets
vivek = {}
print(type(vivek))

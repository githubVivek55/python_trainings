# local & global variables
x = 10  # global variable

def my_function():
    x = 5  # local variable
    print("Inside function:", x)

my_function()

print("Outside function:", x)
# This will work
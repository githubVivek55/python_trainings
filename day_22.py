# list 

marks = [10, 20, 30, 40, 50, "60"]

print(type(marks))
print(marks)

# list comprehension example
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# list comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)

# list comprehension with function
def square(x):
    return x ** 2

squares = [square(x) for x in range(10)]
print("Squares using function:", squares)

# list comprehension with nested loops
nested = [(x, y) for x in range(3) for y in range(2)]
print("Nested list comprehension:", nested)

# list comprehension with if-else
conditional = [x if x%2==0 else x**2 for x in range(10)]
print("Conditional list comprehension:", conditional)

# list comprehension with multiple conditions
multiple_conditions = [x  for x in range(10) if x%2 ==0 if x >5]
print("Multiple conditions list comprehension:", multiple_conditions)

x = [(x,y) for x in range(0,4) for y in range(0,1)]
print("List comprehension with multiple loops:", x)

y =[x if x%2==0 else x**2 for x in range(0,10)]
print("List comprehension with if-else:", y)

# tuple example
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# tuple unpacking example
a, b, c = my_tuple[:3]
print("Unpacked values:", a, b, c)

# tuple comprehension (using generator expression)
tuple_comp = tuple(x**2 for x in range(5))
print("Tuple comprehension:", tuple_comp)


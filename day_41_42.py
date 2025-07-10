# shorthand if else

a = 10
b = 20

c = a if a > b else b
print(c)

# shorthand if else with lambda
max_value = lambda x,y : x if x > y else y
print(max_value(10, 20))
# shorthand if else with lambda and map

# list enumration
list1 = [1, 2, 3, 4, 5]
for index, value in enumerate(list1):
    print(f"Index: {index}, Value: {value}")

# list comprehension
squared_list = [x**2 for x in range(10)]
print(squared_list)
# list comprehension with condition
squared_even_list = [x**2 for x in range(10) if x % 2 == 0]
print(squared_even_list)
# dictionary comprehension
squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)
# dictionary comprehension with condition
squared_even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(squared_even_dict)
# shorthand if else

a = 10
b = 20

c = a if a > b else b
print(c)

# shorthand if else with lambda
max_value = lambda x,y : x if x > y else y
print(max_value(10, 20))
# shorthand if else with lambda and map
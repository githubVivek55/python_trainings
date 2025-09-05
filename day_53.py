# map , reduce and filter
from functools import reduce

l = [1,2,3,4,5,6]

x = lambda x:x**2

even = lambda x:x%2==0
for item in l:
    print(item)

result = map(x,l)

print(list(result))

print(list(filter(even,l)))

sum = reduce(lambda x,y:x+y,l)
print(sum)

# is vs ==
a = 4
b ="4"

print(a==b)
print(a is b)
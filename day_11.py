'''
string litral
'''

a = 'hello'
print(a)
b = "hello"
print(b)
c = '''hello'''
print(c)
d = """hello"""
print(d)
e = '''hello
world'''
print(e)
f = """hello
world"""
print(f)
g = '''hello"
world'''
print(g)

print(g[0])

for i in g:
    print(i, type(i), end="\n")
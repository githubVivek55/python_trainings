class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k;
    def __str__(self):
        return f"{self.i}-{self.j}-{self.k}"
    
    def __add__(self,x):
        return Vector(self.i + x.i, self.j+x.j, self.k+x.k)
    

one = Vector(1,2,4)
print(one)
two = Vector(5,6,7)
print(one+two)
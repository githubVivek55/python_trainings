

class Person:
    def __init__(self,name,occupation,salary):
        self.name = name
        self.occupation = occupation
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        self.__salary = value

    # static method
    @staticmethod
    def getName():
        pass

    def info(self):
        print(f"{self.name}-{self.occupation}-{self.__salary}")

class Animal:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value


vivek = Person("vivek","software dev","20000")
neha = Person("neha","db dev","200000")
vivek.info()
neha.info()
print(vivek.salary)

dog= Animal("Tommy")

Person.getName()
print(dog.name)



# Decorators

def greeting_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before Function")
        result = func(*args,**kwargs)
        print("Done!!")
        return result
    return wrapper

@greeting_decorator
def say_hello():
    print("Hello !!")

@greeting_decorator
def sum(a,b):
    return a+b


print(sum(3,5))


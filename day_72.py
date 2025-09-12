# super 
class Parent:
    def __init__(self, name):
        self.name = name
    
    def parentMethod(self):
        print("parent")

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def childMethod(self):
        super().parentMethod()
        print("Child Method")

childObj = Child("vs")
childObj.childMethod()

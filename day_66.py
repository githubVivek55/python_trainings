# class instance and class variable
class Employee:
    company = "Viks"
    def __init__(self, name):
        self.name = name
    
    def showDetails(self):
        print(f"name id {self.name} - {self.company}")

vs = Employee("vks");
nv = Employee("Nv")
vs.showDetails()
nv.showDetails()
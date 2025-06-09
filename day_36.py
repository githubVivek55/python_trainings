# exception handling

a = input("Enter a number")
try:
    print(int(a))
except Exception as e:
    print(e.__cause__)
except ValueError as v:
    print(v.__notes__)
finally:
    print("always executes")

print("code after error handling")

# custom errors

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message) 
    def __str__(self):
        return f"CustomError: {self.args[0]}"
def raise_custom_error():
    raise CustomError("This is a custom error message")

class CustomError2(Exception):
    def __init__(self, message):
        super().__init__(message)
    def __str__(self):
        return f"Custom error 2 {self.args[0]}"

def raise_custom_error2():
    raise CustomError2("2nd custom error")

try:
    raise_custom_error()
except CustomError as e:
    print(e)

try:
    raise_custom_error2();
except CustomError2 as r:
    print(r)

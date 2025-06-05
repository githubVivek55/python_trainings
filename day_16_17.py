# match case statement

def match_case_example(value):
    match value:
        case 1:
            return "You selected option 1"
        case 2:
            return "You selected option 2"
        case 3:
            return "You selected option 3"
        case _ if value < 1 or value > 3:
            return "Please select a valid option between 1 and 3"
        case _:
            return "Invalid option selected"
        

# Example usage
print(match_case_example(1))
print(match_case_example(2))
print(match_case_example(3))
print(match_case_example(4))

# Day 17 - for loop example

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

name = "vivek"
for char in name:
    print(char)


for i in range(1, 11, 2):
    print(i)

# While loop example
count = 0
while count <5:
    print("Count is :", count)
    count +=1


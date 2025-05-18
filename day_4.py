import pandas

print("Hello World")
print(5)
name=input("Enter your name: ")
print("Hello "+name+ " Welcome here")

should_we_play = input("Do you want to play: ")
answer = should_we_play.lower() == "yes" or should_we_play.lower() == "y"
print(answer)

if answer:
    print("We gonna play")
else:
    print("Thank you, Bye !")

print("This is a test")



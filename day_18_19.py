
# break and continue statements
for i in range(10):
    if i == 5:
        print("Breaking the loop at 5")
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even, skipping")
        continue
    print(f"{i} is odd, processing")

# function
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

# Example usage of the function
print(greet("Alice"))

# function with default parameters
def greet_with_default(name="Guest"):
    """Function to greet a person with a default name."""
    return f"Hello {name}"

print(greet_with_default())

# function with variable number of arguments
def greet_multiple(*names):
    """Function to greet multiple people."""
    greetings = []
    for name in names:
        greetings.append(f"Hello {name}")
    return greetings

result = greet_multiple("Alice", "Bob", "Charlie")
for greeting in result:
    print(greeting)
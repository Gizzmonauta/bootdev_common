r"""
Create a function that accepts a parameter representing a name and returns the message: "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
"""

def greet(name):
    return f"Hello, {name} how are you doing today?"

def main():
    print(greet("Ryan"), "Hello, Ryan how are you doing today?")
    print(greet("Alice"), "Hello, Alice how are you doing today?")
    print(greet("Bob"), "Hello, Bob how are you doing today?")

if __name__ == '__main__':
    main()
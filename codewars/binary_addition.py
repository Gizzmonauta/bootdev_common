r"""
Binary Addition

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""

def add_binary(a, b):
    return format(a + b, 'b')

# Alternative solution using built-in bin function
def add_binary_alt(a, b):
    return bin(a + b)[2:]

r"""
The format() function is a versatile tool for converting values into specific string formats. When you use it for binary conversion, it is essentially acting as a translator between different numbering systems.

Understanding format(value, 'b')
The first argument is the value you want to format (the sum of your two numbers), and the second argument is the format specifier.

The 'b' Type: In Python's formatting language, 'b' stands for Binary. It tells Python: "Take this integer and represent it using base-2 digits (0 and 1)."

The Difference from bin(): While bin(n) always adds the 0b prefix (e.g., "0b1010"), format(n, 'b') gives you the "clean" string (e.g., "1010"), which matches exactly what this kata requires.
"""

def main():
    print(add_binary(1,1),"10")
    print(add_binary(0,1),"1")
    print(add_binary(1,0),"1")
    print(add_binary(2,2),"100")
    print(add_binary(51,12),"111111")

if __name__ == "__main__":
    main()
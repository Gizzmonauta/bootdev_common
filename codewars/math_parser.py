r"""
Instructions
Given a mathematical expression as a string you must return the result as a number.

Numbers
Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.

Operators
You need to support the following mathematical operators:

Multiplication *
Division / (as floating point division)
Addition +
Subtraction -
Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.

Parentheses
You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6

Whitespace
There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (-) used for negating numbers and parentheses will never be separated by whitespace. I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2
1--1   // 2

6 + -(4)   // 2
6 + -( -4) // 10
And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid
Validation
You do not need to worry about validation - you will only receive valid mathematical expressions following the above rules.

Restricted APIs
NOTE: eval and exec are disallowed in your solution.
"""

def calc(expression):
    expr = expression.strip().replace(' ', '')
    print(f"Expression: {expr}")
    operators = set(['+', '-', '*', '/', '(', ')'])
    tokens = []
    current_token = ''
    for i in range(len(expr)):
        char = expr[i]
        if char in operators:
            if current_token:
                tokens.append((float(current_token), 'NUMBER'))
                current_token = ''
            if char == '-' and (i == 0 or expr[i-1] in operators and expr[i-1] != ')'):
                tokens.append((char, 'UNARY_MINUS'))
            elif char == '(':
                tokens.append((char, 'OPEN_PAREN'))
            elif char == ')':
                tokens.append((char, 'CLOSE_PAREN'))
            else:
                tokens.append((char, 'OPERATOR'))
        else:
            current_token += char
    if current_token:
        tokens.append((float(current_token), 'NUMBER'))

    return tokens

def main():
    print(calc("6 + -(4)"))
    print(calc("6 + -( -4)"))
    print(calc("3.14159 * 2.71828 - -(-1.68415)"))
    print(calc("(2 / (2 + 3.33) * 4) - -6.66"))

if __name__ == "__main__":
    main()
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

def calc(expression: str) -> float:
    expr: str = expression.strip().replace(' ', '')
    print(f"Expression: {expr}")
    operators: set[str] = set(['+', '-', '*', '/', '(', ')'])
    tokens: list[tuple[float | str, str]] = []
    current_token: str = ''
    for i in range(len(expr)):
        char: str = expr[i]
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

    if not tokens:
        raise ValueError("Empty expression")
    
    value, _ = parse_expression(tokens, 0)

    return value

def parse_expression(tokens: list[tuple[float | str, str]], index: int) -> tuple[float, int]:
    r'''
    Logic: This function handles the precedence of operators. It first calls parse_factor() to get the first value, then it looks for operators and applies them in the correct order.
        - It first calls parse_term() to get the left-hand side value.
        - Then, it loops. As long as the current token is an OPERATOR tagged + or -, it advances the pointer, calls parse_term() again to get the right-hand side value, and does the math.
    '''
    value, index = parse_term(tokens, index)
    while index < len(tokens) and tokens[index][1] == 'OPERATOR' and tokens[index][0] in ['+', '-']:
        op = tokens[index][0]
        next_value, next_index = parse_term(tokens, index + 1)
        if op == '+':
            value += next_value
        else:
            value -= next_value
        index = next_index
    return value, index

def parse_term(tokens: list[tuple[float | str, str]], index: int) -> tuple[float, int]:
    r'''
    Logic: This function handles the precedence of * and /. It first calls parse_factor() to get the first value, then it looks for operators and applies them in the correct order.
        - It first calls parse_factor() to get the left-hand side value.
        - Then, it loops. As long as the current token is an OPERATOR tagged * or /, it advances the pointer, calls parse_factor() again to get the right-hand side value, and does the math.
    '''
    value, index = parse_factor(tokens, index)
    while index < len(tokens) and tokens[index][1] == 'OPERATOR' and tokens[index][0] in ['*', '/']:
        op = tokens[index][0]
        next_value, next_index = parse_factor(tokens, index + 1)
        if op == '*':
            value *= next_value
        else:
            value /= next_value
        index = next_index
    return value, index

def parse_factor(tokens: list[tuple[float | str, str]], index: int) -> tuple[float, int]:
    r'''
    Logic: This function does the heavy lifting. It looks at the current token:
        - If it is a NUMBER: Return the value and advance the pointer.
        - If it is a UNARY_MINUS: Advance the pointer, then return -1 * parse_factor().
        - If it is an OPEN_PAREN: Advance the pointer, call parse_expression() to solve everything inside the brackets, and finally, advance the pointer past the CLOSE_PAREN
    '''
    if index >= len(tokens):
        raise ValueError("Unexpected end of expression")
    token, token_type = tokens[index]
    if token_type == 'NUMBER':
        return token, index + 1
    elif token_type == 'UNARY_MINUS':
        value, next_index = parse_factor(tokens, index + 1)
        return -value, next_index
    elif token_type == 'OPEN_PAREN':
        value, next_index = parse_expression(tokens, index + 1)
        if next_index >= len(tokens) or tokens[next_index][0] != ')':
            raise ValueError("Expected closing parenthesis")
        return value, next_index + 1
    else:
        raise ValueError(f"Unexpected token: {token}")

def main():
    print(calc("6 + -(4)"))
    print(calc("6 + -( -4)"))
    print(calc("3.14159 * 2.71828 - -(-1.68415)"))
    print(calc("(2 / (2 + 3.33) * 4) - -6.66"))

if __name__ == "__main__":
    main()
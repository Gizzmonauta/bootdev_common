import re

def to_underscore(string):
    # 1. Sanitize: Convert input to string to handle numbers like 1 -> "1"
    s = str(string)
    
    # 2. The Regex Pattern
    # (?<= ...) : Lookbehind - checks if there is a character before the target
    # [^_]: A "Negated Set". This matches any character that is NOT an underscore.
    # [A-Z]  : The Target - finds any Uppercase letter
    # Find a capital letter, strictly preceded by a character that IS NOT an underscore.
    pattern = r'(?<=[^_])[A-Z]'
    
    # 3. The Replacement
    # _      : The underscore we want to insert
    # \g<0>  : A special reference meaning "the character we just matched"
    replacement = r'_\g<0>'
    
    # 4. Execute: Substitute, then lowercase the whole thing
    return re.sub(pattern, replacement, s).lower()

import re

def to_underscore_one_shot(string: str | int) -> str:
    """
    Converts a PascalCase string to snake_case.

    This function inserts an underscore before any uppercase letter that is
    not at the start of the string and not already preceded by an underscore,
    then converts the entire string to lowercase.

    Args:
        string (str | int): The PascalCase string or number to convert.

    Returns:
        str: The string converted to snake_case.

    Examples:
        >>> to_underscore_one_shot("TestController")
        'test_controller'
        >>> to_underscore_one_shot("MoviesAndBooks")
        'movies_and_books'
        >>> to_underscore_one_shot("App7Test")
        'app7_test'
        >>> to_underscore_one_shot(1)
        '1'
    """
    return re.sub(r'(?<=[^_])[A-Z]', r'_\g<0>', str(string)).lower()

def main():
    print(to_underscore("PascalCase"))  # Expected: pascal_case
    print(to_underscore("ThisIsATest"))  # Expected: this_is_a_test
    print(to_underscore("Already_Snake_Case"))  # Expected: already_snake_case
    print(to_underscore("simpleTest"))  # Expected: simple_test
    print(to_underscore("X"))  # Expected: x
    print(to_underscore("Test123Number"))  # Expected: test123_number
    print(to_underscore("TestController"))  # test_controller
    print(to_underscore("MoviesAndBooks"))  # movies_and_books
    print(to_underscore("App7Test"))        # app7_test
    print(to_underscore(1))                 # 1
    print("\n---- Using one-shot function ----")
    print(to_underscore_one_shot("PascalCase"))  # Expected: pascal_case
    print(to_underscore_one_shot("ThisIsATest"))  # Expected: this_is_a_test
    print(to_underscore_one_shot("Already_Snake_Case"))  # Expected: already_snake_case
    print(to_underscore_one_shot("simpleTest"))  # Expected: simple_test
    print(to_underscore_one_shot("X"))  # Expected: x
    print(to_underscore_one_shot("Test123Number"))  # Expected: test123_number
    print(to_underscore_one_shot("TestController"))  # test_controller
    print(to_underscore_one_shot("MoviesAndBooks"))  # movies_and_books
    print(to_underscore_one_shot("App7Test"))        # app7_test
    print(to_underscore_one_shot(1))                 # 1

if __name__ == "__main__":   
    main()
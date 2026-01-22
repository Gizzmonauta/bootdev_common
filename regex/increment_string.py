import re


def increment_string(strng):
    if not isinstance(strng, str):
        raise TypeError("The input should be string")
    # 1. Search for the trailing number (capturing group used)
    match = re.search(r'(\d+)$', strng)
    
    if match:
        # Extract the number part as a string
        number_str = match.group(1)
        
        # 2. measure the length (e.g., "00025" has length 5)
        original_length = len(number_str)
        
        # 3. Do the math
        new_number = int(number_str) + 1
        
        # 4. Pad the new number with zeros to match original length
        # .zfill(5) turns "26" into "00026"
        new_number_str = str(new_number).zfill(original_length)
        
        # Reconstruct the string: Everything before the match + new number
        return strng[:match.start()] + new_number_str
        
    # Fallback: if no number is found, then it ends with a sting, so just append "1"
    return strng + "1"

"""
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
"""

# --- Test Cases ---
print(increment_string("foo00025"))   # Output: foo00026
print(increment_string("Session09"))  # Output: Session10
print(increment_string("Item99"))     # Output: Item100 (zfill expands naturally)
print(increment_string("NoNumber"))   # Output: NoNumber1
print(increment_string("foo"))        # Output: foo1
print(increment_string("foobar001"))  # Output: foobar002
print(increment_string("foobar1"))    # Output: foobar2
print(increment_string("foobar00"))   # Output: foobar01
print(increment_string("foobar99"))   # Output: foobar100
print(increment_string("foobar099"))  # Output: foobar100
print(increment_string("fo99obar99")) # Output: fo99obar100
print(increment_string(""))           # Output: 1
print(increment_string("foobar-1"))   # Output: foobar-2
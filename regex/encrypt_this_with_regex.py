import re

def encrypt_this(text):
    """
    Encrypt this!

    You want to create secret messages which can be deciphered by the Decipher this! kata. 
    Here are the conditions:

    1. Your message is a string containing space separated words.
    2. You need to encrypt each word in the message using the following rules:
    3. The first letter must be converted to its ASCII code.
    4. The second letter must be switched with the last letter
    5. Keepin' it simple: There are no special characters in the input.

    Examples:
    encrypt_this("Hello") == "72olle"
    encrypt_this("good") == "103doo"
    encrypt_this("hello world") == "104olle 119drlo"
    
    Args:
        text (str): The input string containing space separated words.

    ## 2. Constructing the Regex
    This is the core of your assignment. We need a Regex that looks at a word and saves the 
    specific letters we need to swap into Capture Groups.

    Let's build the expression mentally, from left to right, for a standard word like "Hello".

    The Mental Process:

    1. Anchoring: We want to match the whole word from start to finish.

        - Regex: ^...$

        - Explanation: ^ means start of the string, $ means end of the string.

    2. The First Letter: We need to isolate this because it must become a number (ASCII).

        - Regex: ^(\w)...$

        - Explanation: \w matches any word character. Wrapping it in parentheses () creates Group 1.

    3. The Second Letter: We need to isolate this because, according to the rules, this letter must move to the very end.

        - Regex: ^(\w)(\w)...$

        - Explanation: We add another (\w) to capture the second letter. This is Group 2.

    4. The Middle: We need to capture everything between the second letter and the last letter so we can keep it exactly where it is.

        - Regex: ^(\w)(\w)(\w*)...$

        - Explanation: \w* means "zero or more word characters". We use * instead of + because a 3-letter word (like "The") has an empty middle. This is Group 3.
    
    5. The Last Letter: We need to isolate this because it must move to the second position.

        - Regex: ^(\w)(\w)(\w*)(\w)$

        - Explanation: One final (\w) to catch the last character. This is Group 4.
        
    The Final Expression: ^(\w)(\w)(\w*)(\w)$
    """
    # 1. Split the text into a list of words
    words = text.split()
    encrypted_words = []

    for word in words:
        # 2. Check for the complex case (3+ letters) using Regex
        # We look for: Start + First + Second + Middle(optional) + Last + End
        match = re.match(r'^(\w)(\w)(\w*)(\w)$', word)
        
        if match:
            # 3. Capture the distinct parts from the Regex groups
            first_char = match.group(1)
            second_char = match.group(2)
            middle_part = match.group(3)
            last_char = match.group(4)
            
            # 4. Reconstruct: ASCII of first + Last + Middle + Second
            encrypted_word = f"{ord(first_char)}{last_char}{middle_part}{second_char}"
            encrypted_words.append(encrypted_word)
            
        # Handle the edge cases (1 or 2 letters) where the "swap" logic doesn't apply fully
        elif len(word) == 2:
            # ASCII of first + keep the second
            encrypted_words.append(f"{ord(word[0])}{word[1]}")
            
        else:
                # Just ASCII of the first
                encrypted_words.append(f"{ord(word[0])}")

    # 5. Join the list back into a single string
    return " ".join(encrypted_words)

def main():
    # Example usage
    print(encrypt_this("Hello"))        # Output: 72olle
    print(encrypt_this("good"))         # Output: 103doo
    print(encrypt_this("hello world"))  # Output: 104olle 119drlo
    print(encrypt_this("A"))            # Output: 65
    print(encrypt_this("ab"))           # Output: 97b
    print(encrypt_this("Supercalifragilistic spiralidoucious"))  # Output: 83cpercalifragilistiu 115siralidoucioup
    print(encrypt_this("")) # Output: ""
    print(encrypt_this("A wise old owl lived in an oak"))  # Output: 65 119esi 111dl 111lw 108dvei 105n 97n 111ka
    print(encrypt_this("The more he saw the less he spoke"))  # Output: 84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp
    print(encrypt_this("The less he spoke the more he heard"))  # Output: 84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare
    print(encrypt_this("Why can we not all be like that wise old bird"))  # Output: 87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri
    print(encrypt_this("Thank you Piotr for all your help"))  # Output: 84kanh 121uo 80roti 102ro 97ll 121ruo 104ple  
    print(encrypt_this("racecar"))  # Output: 114rcecaa
    print(encrypt_this("step on no pets"))  # Output: 115pet 111n 110o 112ste
    print(encrypt_this("    Somebody        slept                   on           the        space       bar             "))  # Output: 83ymebodo 115tepl 111n 116eh 115eacp 98ra

if __name__ == "__main__":
    main()
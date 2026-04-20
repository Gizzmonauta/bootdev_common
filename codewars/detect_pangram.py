r"""
Detect Pangram

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(st: str) -> bool:
    r"""
    In this solution, we define a string `alphabet` containing all the letters of the English alphabet. We then convert the input string `st` to lowercase and remove any leading or trailing whitespace. We iterate through each character in the processed string, and if it is found in the `alphabet`, we remove that character from `alphabet`. Finally, if `alphabet` is empty, it means all letters were found in the input string, and we return True; otherwise, we return False.
    """
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    text: str = st.strip().lower()
    for char in text:
        if char in alphabet:
            alphabet = alphabet.replace(char, "")
    if not alphabet:
        return True
    return False

def is_pangram_alt(s: str) -> bool:
    r"""
    In this alternative solution, we convert the input string `s` to lowercase. We then iterate through each letter of the English alphabet, and if any letter is not found in the input string, we return False. If all letters are found, we return True.
    """
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

def main():
    print(is_pangram("The quick brown fox jumps over the lazy dog."))
    print(is_pangram("This is not a pangram."))
    print(is_pangram("The quick brown fox jumps over the lazy dog."))
    print(is_pangram("Cwm fjord bank glyphs vext quiz"))
    print(is_pangram("Pack my box with five dozen liquor jugs."))
    print(is_pangram("How quickly daft jumping zebras vex."))
    print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))
    print(is_pangram("This isn't a pangram!"))
    print(is_pangram("abcdefghijklm opqrstuvwxyz"))
    print(is_pangram("Aacdefghijklmnopqrstuvwxyz"))
if __name__ == "__main__":
    main()
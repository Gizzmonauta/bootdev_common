r"""
Decode the Morse code


Instructions
Part of Series 1/3
This kata is part of a series on the Morse code. After you solve this kata, you may move to the next one.
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.

The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS, that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

C: provides parallel arrays, i.e. morse[2] == "-.-" for ascii[2] == "C"
Coffeescript/C++/Crystal/Go/Groovy/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
C#: MorseCode.Get(".--") (returns string)
Elixir: @morse_codes variable (from use MorseCode.Constants). Ignore the unused variable warning for morse_codes because it's no longer used and kept only for old solutions.
Elm: MorseCodes.get : Dict String String
F#: MorseCode.get ".--" (returns string)
Haskell: morseCodes ! ".--" (Codes are in a Map String String)
Java: MorseCode.get(".--")
Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
NASM: a table of pointers to the morsecodes, and a corresponding list of ascii symbols
Racket: morse-code (a hash table)
Rust: MORSE_CODE
Scala: morseCodes(".--")
Swift: MorseCode[".--"] ?? "" or MorseCode[".--", default: ""]
All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions.

Good luck!

After you complete this kata, you may try yourself at Decode the Morse code, advanced.
"""

from ctypes.util import test


MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
    '--..': 'Z', 
    
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
    
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', 
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', 
    '-.-.-.': ';', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '-...-': '=', 
    '.-.-.': '+', '-....-': '-', '..--.-': '_', 
    
    '...---...': 'SOS'
}

def decode_morse(morse_code: str) -> str:
    # you can use the preloaded MORSE_CODE dictionary:
    # letter = MORSE_CODE[morse]
    # For example: 
    #   MORSE_CODE['.-'] = 'A'
    #   MORSE_CODE['--...'] = '7'
    #   MORSE_CODE['...-..-'] = '$'
    words: list[str] = morse_code.strip().split('   ')
    decoded_words: list[str] = []
    for word in words:
        letters: list[str] = word.split(' ')
        decoded_letters: list[str] = []
        for letter in letters:
            if letter in MORSE_CODE:
                decoded_letters.append(MORSE_CODE[letter])
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)

def main():
    print(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
    print(decode_morse('.-'), 'A')
    print(decode_morse('--...'), '7')
    print(decode_morse('...-..-'), '$')
    print(decode_morse('.'), 'E')
    print(decode_morse('..'), 'I')
    print(decode_morse('. .'), 'EE')
    print(decode_morse('.   .'), 'E E')
    print(decode_morse('...-..- ...-..- ...-..-'), '$$$')
    print(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
    print(decode_morse('.-... ---...   -..-. --...'), '&: /7')
    print(decode_morse('...---...'), 'SOS')
    print(decode_morse('... --- ...'), 'SOS')
    print(decode_morse('...   ---   ...'), 'S O S')
    print(decode_morse(' . '), 'E')
    print(decode_morse('   .   . '), 'E E')
    print(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

if __name__ == "__main__":
    main()


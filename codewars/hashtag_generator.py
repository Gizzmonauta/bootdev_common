r"""
The Hashtag Generator

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    - It must start with a hashtag (#).
    - All words must have their first letter capitalized, and remaining letters lowercased.
    - If the final result is longer than 140 chars it must return false.
    - If the input or the result is an empty string it must return false.


Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""

from ctypes.util import test


def generate_hashtag(s: str) -> str:
    if len(s) == 0:
        return False
    list_of_words: list[str] = s.split()
    hashtag: str = '#' + ''.join(word.capitalize() for word in list_of_words)
    if len(hashtag) > 140:
        return False
    if len(hashtag) == 0:
        return False
    return hashtag

def main():
    print(generate_hashtag(" Hello there thanks for trying my Kata"))
    print(generate_hashtag("    Hello     World   "))
    print(generate_hashtag(""))
    print(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
    print(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
    print(generate_hashtag('      Codewars'), '#Codewars', 'Should handle leading whitespace.')
    print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
    print(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
    print(generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.')
    print(generate_hashtag('c i n'), '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.')
    print(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
    print(generate_hashtag(''), False, 'Expected an empty string to return False')
    print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final string is longer than 140 chars.')

if __name__ == '__main__':
    main()
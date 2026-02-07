import re

def top_3_words(text):
    words = re.findall(r"[a-z']*[a-z][a-z']*", text.lower())

    if not words:
        return []

    word_count = {}
    top_3 = [(0,""), (0,""), (0,"")]

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        count = word_count[word]

    for word, count in word_count.items():
        if count > top_3[0][0]:
            top_3[0] = (count, word)
            top_3.sort()

    final_output = [word for count, word in top_3 if count > 0][::-1]
    return final_output

def main():
    print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."), ["a", "of", "on"])
    print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
    print(top_3_words("  //wont won't won't "), ["won't", "wont"])
    print(top_3_words("  , e   .. "), ["e"])
    print(top_3_words("  ...  "), [])
    print(top_3_words("  '  "), [])
    print(top_3_words("  '''  "), [])# 1. Test: Apostrophes as part of a word vs. just punctuation
    print(top_3_words("  '''abc''' ''can't'' 'tis "), ["'tis", "''can't''", "'''abc'''"]) # Wait, let's fix the expected output for clarity
    
    # Refined Stress Tests:
    # 1. Apostrophes surrounding a word (Should strip them or include them based on the 'at least one letter' rule)
    print(top_3_words(" 'abc' 'abc' 'abc' "), ["'abc'"])
    
    # 2. Words with multiple internal apostrophes (Project Manager's 'don't-stop' scenario)
    print(top_3_words(" O'Connor's O'Connor's O'Connor's "), ["o'connor's"])
    
    # 3. Tie-breaking check (Arbitrary ties between words with same count)
    # This checks if your sort() handles words with equal counts correctly.
    print(top_3_words(" apple banana cherry "), ["cherry", "banana", "apple"]) 
    
    # 4. The "One-of-each" case (Ensuring exactly 3 are returned when many unique words have count 1)
    print(top_3_words("one two three four five"), ["two", "three", "one"]) # Order depends on your sort/dictionary order
    
    # 5. Massive "Junk" string (Testing if Regex ignores everything but valid words)
    print(top_3_words(r"12345 !@#$% ^&*() _+ [] {} | \ : ; < > ? , . /"), [])
    
    # 6. Large input with line breaks and tabs (Testing whitespace handling)
    print(top_3_words("line\nline\tline break break"), ["line", "break"])

if __name__ == "__main__":
    main()
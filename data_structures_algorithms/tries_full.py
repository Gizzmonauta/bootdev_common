class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches        

    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = list(current.keys())
            if self.end_symbol in children:
                break
            if len(children) == 1:
                prefix += children[0]
                current = current[children[0]]
            else:
                break
        return prefix

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for key in sorted(current_level):
            if key != self.end_symbol:
                extended_prefix = current_prefix + key
                self.search_level(current_level[key], extended_prefix, words)
        return words

    def words_with_prefix(self, prefix):
        matching_words = []
        current_level = self.root
        for c in prefix:
            if c not in current_level:
                return []
            current_level = current_level[c]
        self.search_level(current_level, prefix, matching_words)
        return matching_words

    def exists(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return True if "*" in current else False

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


# Tests for advanced_find_matches
run_cases = [
    (
        [
            "darnit",
            "nope",
            "bad",
        ],
        "This is a d@rn1t test with b@d words!",
        {
            "@": "a",
            "1": "i",
            "4": "a",
            "!": "i",
        },
        [
            "b@d",
            "d@rn1t",
        ],
    ),
    (
        [
            "darn",
            "shoot",
            "gosh",
        ],
        "h3ck this fudg!ng thing",
        {
            "@": "a",
            "3": "e",
        },
        [],
    ),
    (
        [
            "dang",
            "darn",
            "heck",
            "gosh",
        ],
        "d@ng it to h3ck",
        {
            "@": "a",
            "3": "e",
        },
        ["d@ng", "h3ck"],
    ),
]
submit_cases = run_cases + [
    (
        [
            "darn",
            "shoot",
            "fudging",
        ],
        "sh00t, I hate this fudg!ng assignment",
        {
            "@": "a",
            "3": "e",
            "0": "o",
            "!": "i",
        },
        ["sh00t", "fudg!ng"],
    ),
]


def test(words, document, variations, expected_matches):
    print("---------------------------------")
    print("Document:")
    print(document)
    print(f"Variations: {variations}")
    print(f"Expected matches: {sorted(expected_matches)}")
    try:
        trie = Trie()
        for word in words:
            trie.add(word)
        actual = sorted(trie.advanced_find_matches(document, variations))
        print(f"Actual matches: {actual}")
        if actual == sorted(expected_matches):
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

if __name__ == "__main__":
    main()

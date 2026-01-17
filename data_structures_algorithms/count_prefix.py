"""
Builds a trie from a list of words and counts how many words share a given prefix.

For example:
words = ["apple", "app", "ape", "bat"]
prefix = "ap"
The trie will represent the words, and counting the prefix "ap" will return 3,
as "apple", "app", and "ape" all start with "ap".
"""

def build_trie(words: list[str]) -> dict:
    trie = {"children": {}, "count": 0}
    for word in words:
        current_node: dict = trie
        current_node["count"] += 1
        for char in word:
            if char not in current_node["children"]:
                current_node["children"][char] = {"children": {}, "count": 0}
            current_node = current_node["children"][char]
            current_node["count"] += 1
    return trie

def count_prefix(trie: dict, prefix: str) -> int:
    current_node: dict = trie
    for char in prefix:
        if char not in current_node["children"]:
            return 0
        current_node = current_node["children"][char]
    return current_node["count"]

run_cases = [
    (["apple", "app", "ape", "bat"], "ap", 3),
    (["car", "card", "cart", "dog"], "car", 3),
]

submit_cases = run_cases + [
    ([], "a", 0),
    (["alpha", "beta", "bet", "alphabet"], "", 4),
    (["test", "testing", "tester", "team", "tear"], "te", 5),
    (["foo", "bar", "baz", "foobar", "foobaz"], "foo", 3),
]


def test(words, prefix, expected_output):
    print("---------------------------------")
    print(f"Words:  {words}")
    print(f"Prefix: '{prefix}'")
    print("")
    trie = build_trie(words)
    result = count_prefix(trie, prefix)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
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

main()

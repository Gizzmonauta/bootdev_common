from main import *

run_cases = [
    (
        ["dragon"],
        {
            "dragon": {1: 2, 3: 1},
            "sword": {1: 1, 2: 3},
            "magic": {2: 1},
        },
        [1, 3],
    ),
    (
        ["dragon", "sword"],
        {
            "dragon": {1: 2, 3: 1},
            "sword": {1: 1, 2: 3},
            "magic": {2: 1},
        },
        [1],
    ),
    (
        ["magic", "sword"],
        {
            "dragon": {1: 2, 3: 1},
            "sword": {1: 1, 2: 3},
            "magic": {2: 1},
        },
        [2],
    ),
]

submit_cases = run_cases + [
    (
        ["dragon", "magic"],
        {
            "dragon": {1: 2, 3: 1},
            "sword": {1: 1, 2: 3},
            "magic": {2: 1},
        },
        [],
    ),
    (
        ["shield"],
        {
            "dragon": {1: 2, 3: 1},
            "sword": {1: 1, 2: 3},
            "magic": {2: 1},
        },
        [],
    ),
    (
        ["potion", "quest"],
        {
            "potion": {10: 1, 11: 2, 12: 1},
            "quest": {11: 1, 12: 3},
            "loot": {12: 5},
        },
        [11, 12],
    ),
]


def test(query_terms, inverted_index, expected_output):
    print("---------------------------------")
    print("Input query terms:", query_terms)
    print("Inverted index (term -> {doc_id: term_frequency}):")
    for term in inverted_index:
        print(f"  {term}: {inverted_index[term]}")
    print("")
    result = boolean_search(query_terms, inverted_index)
    print(f"Expected doc IDs: {expected_output}")
    print(f"Actual doc IDs:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
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

main()

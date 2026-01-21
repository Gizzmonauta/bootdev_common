import re


def extract_hashtags(text):
    if text is None:
        return []
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    HASHTAG_PATTERN = re.compile(r"#+?([A-Za-z][A-Za-z0-9_-]*)")
    matches = HASHTAG_PATTERN.findall(text)
    result = []
    if matches:
        for match in matches:
            if "-" not in match:
                result.append(match.lower())
        print(result)
        return result
    return []

def extract_hashtags_solution(text):
    # Find sequences where one or more # are followed by non-whitespace characters
    candidates = re.findall(r"#+(\S+)", text)

    # Regex to validate a cleaned token: starts with letter, then letters/digits/underscores
    valid_pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")

    result = []
    for token in candidates:
        # Strip common trailing punctuation that should not be part of the tag
        cleaned = token.rstrip(".,!?:;)")
        # If the cleaned token exactly matches the valid_pattern, accept it
        if valid_pattern.match(cleaned):
            result.append(cleaned.lower())
    return result

run_cases = [
    (
        "Loving this weather! #SunnyDay #BeachTime",
        ["sunnyday", "beachtime"],
    ),
    (
        "Check out #Python3 and #regex_patterns! Also, avoid #123start and #invalid-tag.",
        ["python3", "regex_patterns"],
    ),
    (
        "Bug fixed in #Version2_0, thanks to #QA and #DevTeam",
        ["version2_0", "qa", "devteam"],
    ),
    (
        "This is not a tag: #1st_place but this is: #first_place",
        ["first_place"],
    ),
]

submit_cases = run_cases + [
    (
        "Mixed content: #HelloWorld, symbols #not-a-tag, and #OK_123!",
        ["helloworld", "ok_123"],
    ),
    (
        "Edge cases: ###triple #_starts_wrong #Valid_One #alsoValid2",
        ["triple", "valid_one", "alsovalid2"],
    ),
    (
        "No tags here, just text and numbers 12345.",
        [],
    ),
]


def test(input_text, expected_output):
    print("---------------------------------")
    print("Input text:")
    print(f"  {input_text}")
    print("")
    result = extract_hashtags(input_text)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
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

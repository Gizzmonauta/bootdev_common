from main import compose, transform_list


def add_1(x):
    return x + 1


def double(x):
    return x * 2


def square(x):
    return x * x


def minus_3(x):
    return x - 3


run_cases = [
    # Simple pipeline: (x * 2) + 1
    ([1, 2, 3], [double, add_1], [3, 5, 7]),
    # Empty transform list should return values unchanged
    ([10, -5, 0], [], [10, -5, 0]),
]

submit_cases = run_cases + [
    # Longer pipeline: ((x + 1)^2) - 3
    ([0, 1, 2, 3], [add_1, square, minus_3], [-2, 1, 6, 13]),
    # Identity pipeline on empty values list
    ([], [square, add_1], []),
    # Single transform only: square
    ([2, -3, 4], [square], [4, 9, 16]),
]


def test(values, transforms, expected_output):
    print("---------------------------------")
    print(f"Input values:      {values}")
    print(f"Number of transforms: {len(transforms)}")
    result = transform_list(values, transforms)
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

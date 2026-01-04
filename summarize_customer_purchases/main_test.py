from main import summarize_purchases

run_cases = [
    (
        [
            {
                "customer": "Alice",
                "items": [
                    {"name": "book", "price": 10, "quantity": 2},
                    {"name": "pen", "price": 2, "quantity": 5},
                ],
            },
            {
                "customer": "Bob",
                "items": [
                    {"name": "notebook", "price": 5, "quantity": 3},
                ],
            },
            {
                "customer": "Alice",
                "items": [
                    {"name": "eraser", "price": 1, "quantity": 4},
                ],
            },
        ],
        {"Alice": 34, "Bob": 15},
    ),
    (
        [
            {
                "customer": "Cara",
                "items": [
                    {"name": "pencil", "price": 1, "quantity": 10},
                ],
            }
        ],
        {"Cara": 10},
    ),
    (
        [],
        {},
    ),
]

submit_cases = run_cases + [
    (
        [
            {
                # missing "customer"
                "items": [
                    {"name": "marker", "price": 3, "quantity": 2},
                ],
            }
        ],
        "ValueError",
    ),
    (
        [
            {
                "customer": "Dave",
                "items": [
                    # missing "quantity"
                    {"name": "ruler", "price": 4},
                ],
            }
        ],
        "ValueError",
    ),
    (
        [
            {
                "customer": "Eve",
                "items": [
                    {"name": "binder", "price": 7, "quantity": 3},  # 21
                    {"name": "stapler", "price": 6, "quantity": 1},  # 6
                ],
            },
            {
                "customer": "Frank",
                "items": [
                    {"name": "paper", "price": 1, "quantity": 50},  # 50
                ],
            },
            {
                "customer": "Eve",
                "items": [
                    {"name": "folder", "price": 2, "quantity": 5},  # 10
                ],
            },
        ],
        {"Eve": 37, "Frank": 50},
    ),
]


def test(input_orders, expected_output):
    print("---------------------------------")
    print("Input orders:")
    for i, order in enumerate(input_orders):
        print(f"  Order {i}:")
        print(f"    customer: {order.get('customer', '<missing>')}")
        print(f"    items:")
        for item in order.get("items", []):
            print(
                f"      - name: {item.get('name', '<missing>')}, "
                f"price: {item.get('price', '<missing>')}, "
                f"quantity: {item.get('quantity', '<missing>')}"
            )
    print("")

    try:
        result = summarize_purchases(input_orders)
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if expected_output == "ValueError":
            print("Fail (expected ValueError but no error was raised)")
            return False
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Expected: {expected_output}")
        print(f"Actual error: {type(e).__name__}: {e}")
        if expected_output == "ValueError" and isinstance(e, ValueError):
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

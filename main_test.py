from main import bfs_traversal

run_cases = [
    (
        "entrance",
        {
            "entrance": ["hall", "armory"],
            "hall": ["kitchen", "library"],
            "armory": ["treasure"],
            "kitchen": [],
            "library": ["treasure"],
            "treasure": [],
        },
        ["entrance", "hall", "armory", "kitchen", "library", "treasure"],
    ),
    (
        "A",
        {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["E"],
            "D": [],
            "E": [],
        },
        ["A", "B", "C", "D", "E"],
    ),
    (
        "A",
        {
            "A": ["B"],
            "B": [],
            "C": ["D"],
            "D": [],
        },
        ["A", "B"],
    ),
]

submit_cases = run_cases + [
    (
        "start",
        {
            "start": ["x", "y"],
            "x": ["z"],
            "y": ["z", "w"],
            "z": [],
            "w": [],
        },
        ["start", "x", "y", "z", "w"],
    ),
    (
        "1",
        {
            "1": ["2", "3"],
            "2": ["4"],
            "3": ["4", "5"],
            "4": ["6"],
            "5": [],
            "6": [],
        },
        ["1", "2", "3", "4", "5", "6"],
    ),
    (
        "hub",
        {
            "hub": ["a", "b", "c"],
            "a": [],
            "b": ["d"],
            "c": [],
            "d": [],
        },
        ["hub", "a", "b", "c", "d"],
    ),
]


def test(start, graph, expected_output):
    print("---------------------------------")
    print("Input graph:")
    for room in graph:
        print(f"  {room} -> {graph[room]}")
    print("")
    print(f"Start room: {start}")
    result = bfs_traversal(start, graph)
    print(f"Expected order: {expected_output}")
    print(f"Actual order:   {result}")
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

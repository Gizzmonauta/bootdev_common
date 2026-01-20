def sum_of_intervals(intervals: list[list]) -> int:
    if not intervals:
        return 0
    ordered_intervals = sorted(intervals)
    current_start, current_end = ordered_intervals[0]
    total = 0
    for start, end in ordered_intervals[1:]:
        if current_end >= start:
            if end > current_end:
                current_end = end
        else:
            total += current_end - current_start
            current_start, current_end = start, end
    total += current_end - current_start
    return total

def test_sum_of_intervals():
    test_cases = [
        {
            "name": "Standard Overlap",
            "input": [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]],
            "expected": 19,
            "note": "Mix of overlaps and disjoints"
        },
        {
            "name": "Touching Intervals",
            "input": [[1, 5], [5, 10]],
            "expected": 9,
            "note": "They touch at 5. Should merge into [1, 10]"
        },
        {
            "name": "Nested Intervals",
            "input": [[1, 10], [2, 5]],
            "expected": 9,
            "note": "[2, 5] is completely inside [1, 10]"
        },
        {
            "name": "Negative Numbers",
            "input": [[-10, -2], [-5, 5]],
            "expected": 15,
            "note": "Merges into [-10, 5]. Length is 5 - (-10) = 15"
        },
        {
            "name": "Large Numbers (Performance)",
            "input": [[-1000000000, 1000000000]],
            "expected": 2000000000,
            "note": "Checks for arithmetic overflow (rare in Python) or memory issues"
        },
        {
            "name": "Zero Length Intervals",
            "input": [[1, 1], [5, 5]],
            "expected": 0,
            "note": "Intervals with no duration should add 0"
        },
        {
            "name": "Mixed Zero and Normal",
            "input": [[1, 5], [2, 2]],
            "expected": 4,
            "note": "The [2, 2] is inside [1, 5] and has 0 length anyway"
        },
        {
            "name": "Empty List",
            "input": [],
            "expected": 0,
            "note": "Should return 0 without crashing"
        }
    ]

    for case in test_cases:
        # We use a copy of the input because sort() modifies in place
        # and we might want to see the original input if it fails
        input_data = [x[:] for x in case["input"]] 
        
        result = sum_of_intervals(input_data)
        
        if result == case["expected"]:
            print(f"✅ {case['name']}: Passed")
        else:
            print(f"❌ {case['name']}: Failed")
            print(f"   Input: {case['input']}")
            print(f"   Expected: {case['expected']}")
            print(f"   Got: {result}")

def main():
    intervals = [[1, 4], [7, 10], [3, 5]]
    print(sum_of_intervals(intervals))
    intervals = [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]
    print(sum_of_intervals(intervals))
    test_sum_of_intervals()

if __name__ == "__main__":
    main()
# Traveling Salesman Problem
# A famous example of a problem in NP is the Traveling Salesman Problem, also known as TSP.

# The version of the problem that we will solve can be stated:
    # Given a list of cities, the distances between each pair of cities, and a total distance, 
    # is there a path through all the cities that is less than the distance given?

def verify_tsp(paths, dist, actual_path):
    sum_dist = 0
    for i in range(1, len(actual_path)):
        sum_dist += paths[actual_path[i-1]][actual_path[i]]
    if sum_dist < dist:
        return True
    return False

def tsp(cities, paths, dist):
    cities_perm = permutations(cities)
    for perm in cities_perm:
        sum_dist = 0
        for i in range(1, len(perm)):
            sum_dist += paths[perm[i-1]][perm[i]]
        if sum_dist < dist:
            return True
    return False

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

run_cases = [
    ([[0, 394], [394, 0]], 3458, [0, 1], True),
    ([[0, 911, 430], [911, 0, 41], [430, 41, 0]], 3104, [1, 2, 0], True),
    ([[0, 10, 1], [10, 0, 1], [1, 1, 0]], 9, [0, 2, 1], True),
]

submit_cases = run_cases + [
    (
        [
            [0, 988, 523, 497],
            [988, 0, 414, 940],
            [523, 414, 0, 802],
            [497, 940, 802, 0],
        ],
        1060,
        [1, 0, 2, 3],
        False,
    ),
    (
        [
            [0, 310, 991, 488, 366],
            [310, 0, 597, 913, 929],
            [991, 597, 0, 223, 516],
            [488, 913, 223, 0, 142],
            [366, 929, 516, 142, 0],
        ],
        3399,
        [0, 1, 3, 4, 2],
        True,
    ),
    (
        [
            [0, 143, 773, 97, 633, 818],
            [143, 0, 256, 931, 545, 722],
            [773, 256, 0, 829, 616, 923],
            [97, 931, 829, 0, 150, 317],
            [633, 545, 616, 150, 0, 101],
            [818, 722, 923, 317, 101, 0],
        ],
        1480,
        [0, 3, 2, 4, 5, 1],
        False,
    ),
]

def print_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        print(mat[i])


def test(paths, dist, actual_path, expected_output):
    try:
        print("---------------------------------")
        print(f"Paths:")
        print_matrix(paths)
        print(f"Checking for a path shorter than {dist}")
        print(f"Using path: {actual_path}")
        result = verify_tsp(paths, dist, actual_path)
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
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

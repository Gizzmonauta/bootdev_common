# Fix Dungeon Map BFS
# The bfs_traversal function is supposed to explore a dungeon map using Breadth First Search (BFS).

# The dungeon is represented as a dictionary where:

# each key is a room name (a string)
# each value is a list of rooms that are directly connected to it
# bfs_traversal(start, graph) should return a list of room names in the order they are visited by BFS.

# Right now, the function is exploring one path as deep as possible before coming back to explore other rooms. That is Depth First behavior, not Breadth First.

# Your job: fix bfs_traversal so that it correctly performs BFS.


def bfs_traversal(start, graph):
    visited_list = [start]
    neighbor_queue = graph[start]
    while neighbor_queue:
        next_room = neighbor_queue.pop(0)
        if next_room not in visited_list:
            visited_list.append(next_room)
        neighbor_queue.extend(graph[next_room])
    return visited_list


# def bfs_traversal(start, graph):
#     visited = set()
#     result = []

#     queue = [start]

#     while queue:
#         current = queue.pop(0)

#         if current in visited:
#             continue

#         visited.add(current)
#         result.append(current)

#         neighbors = graph.get(current, [])
#         for neighbor in neighbors:
#             if neighbor not in visited:
#                 queue.append(neighbor)

#     return result


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

if __name__ == "__main__":
    main()
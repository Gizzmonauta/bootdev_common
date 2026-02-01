r"""
Find Shortest Path in Graph
Complete the shortest_path function.

You are given a directed graph as a dictionary (map) in Python. Each key is a node, and its value is a list of nodes it has edges to.

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

Your job is to return the shortest path from a start node to a goal node as a list of node names, using a breadth-first search (BFS) style approach.

If there is no path, return an empty list [].

If start and goal are the same node, return a list containing just that node (as long as it exists in the graph).

-------------------------------------------------------------------------
Function Details
Implement this function in main.py:

def shortest_path(start, goal, graph):
    # your code here

start – the name of the starting node (string)
goal – the name of the target node (string)
graph – a dictionary mapping node names (strings) to lists of neighbor node names (strings)
Return value:

A list of node names representing the nodes on the shortest path from start to goal, including both start and goal.
If there is no path, return [].
You should treat the graph as directed: edges go only in the direction listed in the neighbors.

-------------------------------------------------------------------------
Expected Behavior
Use a BFS-style search to find the shortest path (fewest edges).

Handle these cases:

start or goal is not in the graph → return [].
start == goal and the node exists in the graph → return [start].
There is at least one path → return one shortest path as a list.
There is no path → return [].
You can keep track of the path by remembering where you came from for each visited node, then rebuilding the path from goal back to start at the end.

-------------------------------------------------------------------------
Examples
Example 1: Simple path
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print(shortest_path("A", "D", graph))
# ["A", "B", "D"]  (or ["A", "C", "D"] would also be a valid shortest path,
# but with this graph order a BFS will naturally find ["A", "B", "D"] first)

Example 2: No path
graph = {
    "A": ["B"],
    "B": [],
    "C": ["D"],
    "D": []
}

print(shortest_path("A", "D", graph))
# []   (no path from A to D in this directed graph)

Example 3: Start equals goal
graph = {
    "X": ["Y"],
    "Y": []
}

print(shortest_path("X", "X", graph))
# ["X"]
"""

def shortest_path(start: str, goal: str, graph: dict[list]) -> list:
    if start not in graph or goal not in graph:
        return []
    if start == goal:
        return [start]

    visited: set = {start}

    queue: list = []
    queue.append([start])

    while len(queue) > 0:
        current_path: list = queue[0]
        del queue[0]

        tail: str = current_path[-1]

        # Get neighbors
        # We use graph.get(tail, []) just in case a node creates a dead end 
        # that wasn't defined as a key in the dictionary (robustness)
        neighbors = graph.get(tail, [])

        sorted_adjacent_nodes: list = sorted(neighbors)
        for san in sorted_adjacent_nodes:
            if san not in visited:
                visited.add(san)
                new_path = current_path + [san]
                if san == goal:
                    return new_path
                queue.append(new_path)
    return []


run_cases = [
    (
        "A",
        "D",
        {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"],
            "D": [],
        },
        ["A", "B", "D"],
    ),
    (
        "A",
        "D",
        {
            "A": ["B"],
            "B": [],
            "C": ["D"],
            "D": [],
        },
        [],
    ),
]

submit_cases = run_cases + [
    (
        "X",
        "X",
        {
            "X": ["Y"],
            "Y": ["Z"],
            "Z": [],
        },
        ["X"],
    ),
    (
        "A",
        "F",
        {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D", "E"],
            "D": ["F"],
            "E": ["F"],
            "F": [],
        },
        ["A", "B", "D", "F"],
    ),
]


def test(start, goal, graph, expected_output):
    print("---------------------------------")
    print("Input graph:")
    for node in sorted(graph.keys()):
        print(f"  {node} -> {graph[node]}")
    print("")
    print(f"Start: {start}")
    print(f"Goal:  {goal}")
    result = shortest_path(start, goal, graph)
    print("")
    print(f"Expected path: {expected_output}")
    print(f"Actual path:   {result}")
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

# from collections import deque

# def shortest_path(start: str, goal: str, graph: dict) -> list:
#     if start not in graph or goal not in graph:
#         return []
#     if start == goal:
#         return [start]

#     # 1. QUEUE: Use deque for O(1) pops
#     queue = deque([start])
    
#     # 2. VISITED + PATHS: Key=Node, Value=Parent
#     # We use this single dict to track 'visited' AND to rebuild the path later.
#     # We map 'start' to None because it has no parent.
#     predecessors = {start: None}

#     while queue:
#         current_node = queue.popleft() # O(1) speed!

#         if current_node == goal:
#             break # Goal found!

#         # Safety .get() used here
#         for neighbor in graph.get(current_node, []):
#             if neighbor not in predecessors:
#                 predecessors[neighbor] = current_node # Record where we came from
#                 queue.append(neighbor)
    
#     # 3. Reconstruct path backwards (only if we found the goal)
#     if goal in predecessors:
#         path = []
#         node = goal
#         while node is not None:
#             path.append(node)
#             node = predecessors[node]
#         return path[::-1] # Reverse to get Start -> Goal
        
#     return []

r"""
1. What is a deque?
It stands for "Double-Ended Queue" (pronounced like "deck" of cards).

Think of a standard Python list like a stack of heavy books.
* Adding to the top (append): Easy. You just place a book on top.
* Removing from the bottom (index 0): Very hard. To take the bottom book out, you have to lift every single other book and shift them down.

Now, think of a deque like a ticket roll or a line of people.

* Adding to the back: Easy.
* Removing from the front: Easy. You just tear off the next ticket. No one has to shift or move.

2. Why do we need it for BFS?
Breadth-First Search (BFS) is a "First-In, First-Out" (FIFO) algorithm. You always process the node that has been waiting the longest (the one at the front of the line).
* Using a List (list.pop(0)): Python has to physically shift every remaining element in memory one spot to the left to fill the gap. If your queue has 10,000 items, that’s 10,000 operations just to remove one item!
    * Time Complexity: $O(N)$ (Linear - Slow)
* Using a Deque (deque.popleft()): Python just moves a pointer. It doesn't shift anything. It takes the same amount of time whether the queue has 5 items or 5 million items.
    * Time Complexity: $O(1)$ (Constant - Fast)
"""
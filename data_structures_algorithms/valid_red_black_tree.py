class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color  # "R" or "B"
        self.left = None
        self.right = None


def is_valid_red_black_tree(root):
    """Return True if the tree rooted at `root` is a valid red–black tree."""
    if root is None:
        return True
    if root.color != "B":
        return False
    
    def check_properties(node):
        if node is None:
            return 1  # Black height of null nodes is 1
        if node.color not in ("R", "B"):
            return -1  # Invalid color
        left_black_height = check_properties(node.left)
        right_black_height = check_properties(node.right)
        if left_black_height == -1 or right_black_height == -1:
            return -1  # Propagate failure
        if left_black_height != right_black_height:
            return -1  # Black heights differ
        if node.color == "R":
            if (node.left and node.left.color == "R") or (node.right and node.right.color == "R"):
                return -1  # Red node with red child
        return left_black_height + (1 if node.color == "B" else 0)

    return check_properties(root) != -1 

def describe_tree(root):
    levels = []

    def walk(node, depth):
        while len(levels) <= depth:
            levels.append([])
        if node is None:
            levels[depth].append("None")
            return
        label = str(node.value) + node.color
        levels[depth].append(label)
        if node.left is None and node.right is None:
            return
        walk(node.left, depth + 1)
        walk(node.right, depth + 1)

    walk(root, 0)
    lines = []
    for depth in range(len(levels)):
        line = "Level " + str(depth) + ": " + ", ".join(levels[depth])
        lines.append(line)
    return "\n".join(lines)


def make_simple_valid_tree():
    root = Node(10, "B")
    root.left = Node(5, "R")
    root.right = Node(15, "R")
    return root


def make_root_red_tree():
    root = Node(10, "R")
    root.left = Node(5, "B")
    root.right = Node(15, "B")
    return root


def make_red_red_child_tree():
    root = Node(10, "B")
    root.left = Node(5, "R")
    root.right = Node(15, "B")
    root.left.left = Node(2, "R")
    return root


def make_bad_black_height_tree():
    root = Node(10, "B")
    root.left = Node(5, "B")
    root.right = Node(15, "B")
    root.left.left = Node(2, "R")
    root.left.right = None
    root.right.right = Node(20, "R")
    root.right.right.right = Node(25, "B")
    return root


run_cases = [
    (None, True, "Empty tree"),
    (make_simple_valid_tree(), True, "Simple valid RB tree"),
]

submit_cases = run_cases + [
    (make_root_red_tree(), False, "Root must be black"),
    (make_red_red_child_tree(), False, "Red node with red child"),
    (make_bad_black_height_tree(), False, "Mismatched black heights"),
    (make_simple_valid_tree(), True, "Valid tree again (sanity check)"),
]


def test(root, expected, label):
    print("---------------------------------")
    print("Case:", label)
    print("Tree:")
    if root is None:
        print("  <empty tree>")
    else:
        print(describe_tree(root))
    result = is_valid_red_black_tree(root)
    print("")
    print("Expected:", expected)
    print("Actual:  ", result)
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for root, expected, label in test_cases:
        correct = test(root, expected, label)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    if skipped > 0:
        print(str(passed) + " passed, " + str(failed) + " failed, " + str(skipped) + " skipped")
    else:
        print(str(passed) + " passed, " + str(failed) + " failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()


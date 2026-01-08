import random
from main import *
from user import *

run_cases = [
    (4),
]

submit_cases = run_cases + [
    (10),
]


def validate_tree_structure(node, tree):
    """Validate the tree maintains proper BST and parent-child relationships."""
    if node.val is None:  # nil node
        return True
    
    # Check parent-child relationships
    if node.left.val is not None:
        if node.left.parent != node:
            return False
        if not (node.left.val < node.val):
            return False
    
    if node.right.val is not None:
        if node.right.parent != node:
            return False
        if not (node.right.val > node.val):
            return False
    
    # Recursively check children
    return (validate_tree_structure(node.left, tree) and 
            validate_tree_structure(node.right, tree))


def test_rotate(tree, node, direction):
    print(f"Rotating {direction} at {node.val}...")
    print("-------------------------------------")
    print("Tree before rotation:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")
    
    if direction == "left":
        tree.rotate_left(node)
    else:
        tree.rotate_right(node)
    
    print("Tree after rotation:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")
    
    # Validate the tree structure is still valid
    if not validate_tree_structure(tree.root, tree):
        print("✗ Tree structure invalid after rotation")
        return False
    
    print("✓ Tree structure valid after rotation")
    return True


def test_rotations(tree):
    results = []
    
    # Test left rotation at root
    if tree.root.right.val is not None:
        results.append(test_rotate(tree, tree.root, "left"))
    else:
        print("Skipping left rotation at root (no right child)")
        results.append(True)
    
    # Test right rotation at root
    if tree.root.left.val is not None:
        results.append(test_rotate(tree, tree.root, "right"))
    else:
        print("Skipping right rotation at root (no left child)")
        results.append(True)
    
    # Test left rotation at root.right
    if tree.root.right.val is not None and tree.root.right.right.val is not None:
        results.append(test_rotate(tree, tree.root.right, "left"))
    else:
        print("Skipping left rotation at root.right")
        results.append(True)
    
    # Test right rotation at root.left
    if tree.root.left.val is not None and tree.root.left.left.val is not None:
        results.append(test_rotate(tree, tree.root.left, "right"))
    else:
        print("Skipping right rotation at root.left")
        results.append(True)
    
    return all(results)


def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    for user in users:
        tree.insert(user)
    print("=====================================")
    print("Starting Tree:")
    print("-------------------------------------")
    print_tree(tree)
    print("-------------------------------------")

    if test_rotations(tree):
        print("Pass \n")
        return True
    print("Fail \n")
    return False


def format_tree_string(node, lines, level=0):
    if node.val is not None:
        format_tree_string(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        format_tree_string(node.left, lines, level + 1)


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    print("\n".join(lines))


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
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

from main import *
from user import *

run_cases = [
    (4),
]

submit_cases = run_cases + [
    (10),
]


def count_black_height(node, tree):
    """Count black nodes from node to any leaf. Returns -1 if inconsistent."""
    if node.val is None:  # nil node
        return 1
    
    left_height = count_black_height(node.left, tree)
    right_height = count_black_height(node.right, tree)
    
    if left_height == -1 or right_height == -1 or left_height != right_height:
        return -1
    
    return left_height + (1 if not node.red else 0)


def validate_rb_properties(node, tree):
    """Validate Red-Black Tree properties."""
    if node.val is None:
        return True
    
    # Property 4: If a node is red, both children must be black
    if node.red:
        if (node.left.val is not None and node.left.red) or \
           (node.right.val is not None and node.right.red):
            print(f"✗ Red node {node.val} has red child")
            return False
    
    # Check BST property
    if node.left.val is not None and not (node.left.val < node.val):
        print(f"✗ BST violation: left child {node.left.val} >= parent {node.val}")
        return False
    
    if node.right.val is not None and not (node.right.val > node.val):
        print(f"✗ BST violation: right child {node.right.val} <= parent {node.val}")
        return False
    
    return validate_rb_properties(node.left, tree) and validate_rb_properties(node.right, tree)


def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    for user in users:
        tree.insert(user)
    print("=====================================")
    print(f"Inserted {num_users} users: {users}")
    print("-------------------------------------")
    print("Tree:")
    print("-------------------------------------")
    print(print_tree(tree))
    print("-------------------------------------\n")

    # Validate RB properties
    all_valid = True
    
    # Property 2: Root is black
    if tree.root.val is not None and tree.root.red:
        print("✗ Root is red (should be black)")
        all_valid = False
    else:
        print("✓ Root is black")
    
    # Property 4: No red node has red children
    if not validate_rb_properties(tree.root, tree):
        all_valid = False
    else:
        print("✓ No red node has red children")
    
    # Property 5: All paths have same black height
    black_height = count_black_height(tree.root, tree)
    if black_height == -1:
        print("✗ Inconsistent black heights")
        all_valid = False
    else:
        print(f"✓ Consistent black height: {black_height}")
    
    # Check in-order traversal is sorted
    inorder = []
    def traverse(node):
        if node.val is not None:
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
    traverse(tree.root)
    
    if inorder == sorted(users):
        print("✓ In-order traversal is sorted")
    else:
        print("✗ In-order traversal not sorted")
        all_valid = False

    if all_valid:
        print("Pass \n")
        return True
    print("Fail \n")
    return False


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    return "\n".join(lines)


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

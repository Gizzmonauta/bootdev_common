class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        current = new_node
        while current.parent is not None and current.parent.red:
            parent = current.parent
            grandparent = parent.parent
            if parent == grandparent.right:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent
                else:
                    if current == parent.left:
                        current = parent
                        self.rotate_right(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
            elif parent == grandparent.left:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent
                else:
                    if current == parent.right:
                        current = parent
                        self.rotate_left(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot



# In addition to all the rules of a Binary Search Tree, a red-black tree must follow some additional ones:

#   1. Each node is either red or black
#   2. The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
#   3. All Nil leaf nodes are black.
#   4. If a node is red, then both its children are black.
#   5. All paths from a single node go through the same number of black nodes to reach any of its descendant NIL nodes.
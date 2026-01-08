class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def height(self):
        if self.val is None:
            return 0
        lh: int = 0
        rh: int = 0
        if self.left is not None:
            lh = self.left.height()
        if self.right is not None:
            rh = self.right.height()
        return max(lh, rh) + 1

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)
    
    def inorder(self, visited):
        if self.left is not None:
            self.left.inorder(visited)
        if self.val is not None:
            visited.append(self.val)
        if self.right is not None:
            self.right.inorder(visited)
        return visited

    def postorder(self, visited):
        if self.left is not None:
            self.left.postorder(visited)
        if self.right is not None:
            self.right.postorder(visited)
        if self.val is not None:
            visited.append(self.val)
        return visited
    
    def preorder(self, visited):
        if self.val is not None:
            visited.append(self.val)
        if self.left is not None:
            self.left.preorder(visited)
        if self.right is not None:
            self.right.preorder(visited)
        return visited

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
            return self
        elif val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
            return self
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            successor = self.right
            while successor.left is not None:
                successor = successor.left
            self.val = successor.val
            self.right = self.right.delete(successor.val)
            return self

    def get_min(self):
        if self.val is None:
            raise ValueError("Cannot get min from an empty tree")
        current_min = self
        while current_min.left != None:
            current_min = current_min.left
        return current_min.val

    def get_max(self):
        if self .val is None:
            raise ValueError("Cannot get max from an empty tree")
        current_max = self
        while current_max.right != None:
            current_max = current_max.right
        return current_max.val



# One of the most common types of ordered tree is a Binary Search Tree or BST. A BST has some additional constraints:

#     1. Instead of an unbounded list of children, each node has at most 2 children
#     2. The left child's value must be less than its parent's value
#     3. The right child's value must be greater than its parent's value
#     4. No two nodes in the BST can have the same value

#                                      12
#                                    /    \
#                                   /      \
#                                  7        30
#                                /   \     /  \
#                               /     \   /    \
#                              1      10 20    80
#                               \     /   \
#                                \   /     \
#                                 6 8       25

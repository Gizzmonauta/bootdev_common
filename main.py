class BSTNode:
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
        

    # don't touch below this line

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

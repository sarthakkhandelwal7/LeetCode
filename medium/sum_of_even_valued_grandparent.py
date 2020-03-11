class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode, parent=1, grand_parent=1) -> int:
        if root is None:
            return 0
        return self.sumEvenGrandparent(root.left, root.val, parent) + self.sumEvenGrandparent(root.right, root.val, parent) + (root.val if grand_parent % 2 == 0 else 0)

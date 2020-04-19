# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def buildTree(preorder, inorder) -> TreeNode:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        preorder = collections.deque(preorder)

        def generate_tree(left, right):
            if not preorder: return
            node = preorder.popleft()
            index = inorder_index[node]
            root = TreeNode(node)
            if left != index:
                root.left = generate_tree(left, index-1)
            if right != index:
                root.right = generate_tree(index+1, right)

            return root
        return generate_tree(0, len(inorder)-1)

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        n1 = n2 = None

        def dfs(prev, node, level):
            nonlocal n1, n2
            if not node:
                return None
            node.parent = prev
            node.level = level
            if node.val == x:
                n1 = node

            if node.val == y:
                n2 = node

            dfs(node, node.left, level + 1)
            dfs(node, node.right, level + 1)

        dfs(None, root, 0)
        return n1.parent != n2.parent and n1.level == n2.level


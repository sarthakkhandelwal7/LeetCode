class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 1

        def dfs(node):
            nonlocal ans
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            ans = max(ans, l + r + 1)
            return max(l, r) + 1

        dfs(root)
        return ans - 1
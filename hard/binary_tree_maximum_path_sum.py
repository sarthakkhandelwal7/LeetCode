class Solution:
    def maxPathSum(self, root: TreeNode):
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            l_sum = max(dfs(node.left), 0)
            r_sum = max(dfs(node.right), 0)
            max_sum = max(max_sum, l_sum + r_sum + node.val)

            return max(l_sum, r_sum) + node.val

        dfs(root)
        return max_sum

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []

        def traverse(root, level):
            if root:
                if level == len(ans):
                    ans.append(root.val)

                traverse(root.right, level + 1)
                traverse(root.left, level + 1)

        traverse(root, 0)
        return ans
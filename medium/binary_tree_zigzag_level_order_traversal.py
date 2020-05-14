from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        ans = []

        def level_order_trav(node, level):
            if not node:
                return None

            if level >= len(ans):
                ans.append(deque())

            if level % 2 == 0:
                ans[level].append(node.val)

            else:
                ans[level].appendleft(node.val)

            level_order_trav(node.left, level + 1)
            level_order_trav(node.right, level + 1)

        level_order_trav(root, 0)
        return ans

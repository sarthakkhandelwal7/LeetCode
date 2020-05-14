from collections import deque


class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []
        left_tree = deque()
        right_tree = deque()
        right_tree.append([])

        def traverse(node, x, y):
            if node:
                if x < 0:
                    if len(left_tree) < abs(x) or len(left_tree) == 0:
                        left_tree.appendleft([])
                    left_tree[x].append((y, node.val))

                else:
                    if len(right_tree) <= x:
                        right_tree.append([])
                    right_tree[x].append((y, node.val))

                traverse(node.left, x - 1, y + 1)
                traverse(node.right, x + 1, y + 1)

        traverse(root, 0, 0)
        ans = left_tree + right_tree
        return [[val for _, val in sorted(col)] for col in ans]
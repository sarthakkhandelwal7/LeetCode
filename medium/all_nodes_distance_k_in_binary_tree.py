class Solution:
    def distanceK(self, root_node, target, k: int):
        ans = list()

        def helper(node):
            if not node:
                return -1

            elif node == target:
                check_sub_tree(node, 0)
                return 1

            else:
                l, r = helper(node.left), helper(node.right)
                if l != -1:
                    if l == k: ans.append(node.val)
                    check_sub_tree(node.right, l + 1)
                    return l + 1

                elif r != -1:
                    if r == k: ans.append(node.val)
                    check_sub_tree(node.left, r + 1)
                    return r + 1

                else:
                    return -1

        def check_sub_tree(root, distance):
            if not root:
                return

            elif k == distance:
                ans.append(root.val)

            else:
                check_sub_tree(root.left, distance + 1)
                check_sub_tree(root.right, distance + 1)

        helper(root_node)
        return ans
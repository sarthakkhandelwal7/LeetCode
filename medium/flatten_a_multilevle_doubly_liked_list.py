# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        if not head:
            return head

        def helper(prev, curr):
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            temp = curr.next
            tail = helper(curr, curr.child)
            curr.child = None
            return helper(tail, temp)

        pseudo_head = Node(0, None, head, None)
        helper(pseudo_head, head)
        pseudo_head.next.prev = None

        return pseudo_head.next
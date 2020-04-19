class ListNode:
    def __init__(self, node):
        self.next = node


class Solution:
    @staticmethod
    def reverseBetween(head: ListNode, m: int, n: int):
        if not head:
            return None

        n = n - m

        previous = pseudo_head = ListNode(head)
        curr = head

        while m != 1:
            previous, curr = curr, curr.next
            m -= 1

        def reverse_list(node, i):
            prev = curr_node = node
            while i:
                i -= 1
                curr_node.next, prev, curr_node = prev, curr_node, curr_node.next

            tail, curr_node.next = curr_node.next, prev
            return curr_node, tail

        previous.next, curr.next = reverse_list(curr, n)
        return pseudo_head.next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        previous = None
        nxt = curr = head
        count = 0
        node = curr
        while node and count < k:
            node = node.next
            count += 1
        if count != k:
            return head

        # Reversing k-nodes
        while count:
            nxt = nxt.next
            curr.next = previous
            previous = curr
            curr = nxt
            count -= 1
        head.next = self.reverseKGroup(curr, k)
        return previous

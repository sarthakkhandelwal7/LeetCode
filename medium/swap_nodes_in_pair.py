class Solution:
    def swapPairs(self, head):
        previous = curr = head
        i = 0
        if not curr or not curr.next:
            return head
        while i < 2:
            curr.next, curr, previous = previous, curr.next, curr
            i += 1
        head.next = self.swapPairs(curr)
        return previous

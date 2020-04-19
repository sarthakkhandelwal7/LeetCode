class Solution:
    @staticmethod
    def split(head):
        previous = slow = fast = head
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        previous.next = None
        return slow

    @staticmethod
    def reverse_linked_list(head):
        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def reorderList(self, head) -> None:
        if not head or not head.next:
            return

        middle_node = self.split(head)
        next = self.reverse_linked_list(middle_node)

        curr = head
        while next:
            temp = curr.next
            curr.next = next
            next = temp
            curr = curr.next

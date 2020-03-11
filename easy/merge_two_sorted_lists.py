# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        head = curr = ListNode(None)
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        curr.next = curr1 or curr2
        return head.next


def prt(head):
    st = ''
    curr = head
    while curr:
        st += f'{curr.val}-->'
        curr = curr.next
    # return st[:len(st)-3]
    print(st[:len(st)-3])


if __name__ == '__main__':
    l1 = None
    l2 = ListNode(0)
    node = Solution().mergeTwoLists(l1, l2)
    print(prt(node))

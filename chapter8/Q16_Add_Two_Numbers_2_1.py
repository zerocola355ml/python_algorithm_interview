# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        up = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or up > 0:
            if l1 and l2:
                up, val = divmod(l1.val + l2.val + up, 10)
            elif l1:
                up, val = divmod(l1.val + up, 10)
            elif l2:
                up, val = divmod(l2.val + up, 10)
            elif up > 0:
                up, val = 0, up
            curr.next = ListNode(val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
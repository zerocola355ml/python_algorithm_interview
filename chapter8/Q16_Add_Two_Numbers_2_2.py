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
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            up, val = divmod(val + up, 10)

            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
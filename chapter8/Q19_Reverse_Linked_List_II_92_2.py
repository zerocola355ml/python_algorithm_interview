# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode()
        curr = dummy
        dummy.next = head

        for _ in range(left - 1):
            curr = curr.next
        start = curr
        end = start.next
        nxt = end.next

        for _ in range(right - left):
            nxt.next, end, nxt = end, nxt, nxt.next

        start.next.next = nxt
        start.next = end

        return dummy.next
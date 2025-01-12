# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev, curr, nxt = dummy, head, head.next

        while nxt:
            prev.next, nxt.next, prev, curr = nxt, curr, curr, nxt.next
            if curr:
                nxt = curr.next
            else:
                prev.next = None
                break
        if curr:  # odd case
            prev.next = curr

        return dummy.next
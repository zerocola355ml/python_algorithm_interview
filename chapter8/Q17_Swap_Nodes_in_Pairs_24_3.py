# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = head
        result = prev

        while head and head.next:
            curr = head.next
            head.next = curr.next
            curr.next = head
            prev.next = curr
            head = head.next
            prev = prev.next.next

        return result.next
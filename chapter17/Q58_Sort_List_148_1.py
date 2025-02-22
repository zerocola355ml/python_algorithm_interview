# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        curr = head
        idx = 0

        while curr:
            heapq.heappush(heap, (curr.val, idx, curr))
            curr = curr.next
            idx += 1

        head = ListNode()
        curr = head

        while heap:
            curr.next = heapq.heappop(heap)[2]
            curr = curr.next
        curr.next = None
        return head.next
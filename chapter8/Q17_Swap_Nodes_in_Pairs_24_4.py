# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, one: Optional[ListNode]) -> Optional[ListNode]:
        if one and one.next:
            two = one.next
            one.next = self.swapPairs(two.next)
            two.next = one
            return two
        return one

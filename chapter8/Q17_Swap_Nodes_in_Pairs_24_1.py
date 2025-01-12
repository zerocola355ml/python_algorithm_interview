# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(one):
            if not one or not one.next:
                return one
            three = one.next.next
            one.next.next = one
            two = one.next
            one.next = helper(three)
            return two

        return helper(head)

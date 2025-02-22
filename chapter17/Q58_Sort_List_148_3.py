# Answer2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = ans = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next

        vals.sort()

        for val in vals:
            ans.val = val
            ans = ans.next

        return head
# My solutions1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-float("inf"))
        dummy.next = head
        last = head
        while last.next:
            if last.val <= last.next.val:
                last = last.next
            else:
                curr = last.next
                last.next = last.next.next
                before = dummy
                while before.next.val <= curr.val:
                    before = before.next
                curr.next, before.next = before.next, curr

        return dummy.next
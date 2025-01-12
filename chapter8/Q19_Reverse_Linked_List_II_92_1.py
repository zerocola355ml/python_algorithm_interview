# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        curr = head
        prev = None
        left_end = None
        right_start = None

        while curr:
            if index == left - 1:
                left_end = curr
            elif index == left:
                middle_end = curr
            if index < left:
                curr = curr.next
            elif left <= index <= right:
                curr.next, curr, prev = prev, curr.next, curr
            elif index == right + 1:
                right_start = curr
                curr = curr.next
            if index > right:
                break
            index += 1

        if left_end:
            left_end.next = prev
        else:
            head = prev

        middle_end.next = right_start

        return head
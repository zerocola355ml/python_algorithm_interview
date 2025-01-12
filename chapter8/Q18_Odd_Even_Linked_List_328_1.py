# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = head.next
        curr = head.next.next

        while curr and curr.next:
            odd.next = curr
            even.next = curr.next
            odd = odd.next
            even = even.next
            curr = curr.next.next

        if curr:
            odd.next = curr
            odd = odd.next

        odd.next = even_head
        even.next = None  # 처음에 이 부분 빠트려서 루프 생김.

        return head

# My solution1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return

        result = ListNode(0)
        curr = result

        while True:
            min_head = ListNode(float("inf"))
            min_index = -1
            for i, head in enumerate(lists):
                if head and head.val < min_head.val:
                    min_head = head
                    min_index = i

            if min_index >= 0:
                curr.next = min_head
                curr = curr.next
                # min_head = min_head.next #이건 안되고
                lists[min_index] = lists[min_index].next  # 이건 되네?
            else:
                break
        return result.nex
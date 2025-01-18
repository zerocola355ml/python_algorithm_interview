# My solutions2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        root = ListNode()
        curr = root

        while None in lists:
            lists.remove(None)

        while lists:
            lists = sorted(lists, key=lambda node: node.val, reverse=True)
            node = lists[-1]
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                lists[-1] = node
            else:
                lists.pop()

        return root.next
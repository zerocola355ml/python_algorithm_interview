# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 새로운 더미 노드 생성 (결합된 리스트의 시작점 역할)
        new = ListNode(0)
        curr = new  # 현재 노드를 더미 노드로 초기화

        # 두 리스트를 순회하며 병합
        while l1 and l2:  # 두 리스트 모두 노드가 남아 있는 동안 반복
            if l1.val < l2.val:  # l1의 값이 l2의 값보다 작으면
                curr.next = l1  # 현재 노드의 다음을 l1로 설정
                l1 = l1.next  # l1을 다음 노드로 이동
            else:  # l2의 값이 더 작거나 같으면
                curr.next = l2  # 현재 노드의 다음을 l2로 설정
                l2 = l2.next  # l2를 다음 노드로 이동
            curr = curr.next  # 현재 노드를 다음으로 이동

        # l1 또는 l2에 남은 노드가 있다면 그대로 연결
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        # 더미 노드의 다음 노드(실제 병합된 리스트의 시작)를 반환
        return new.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 빈 리스트는 항상 palindrome
        if not head:
            return True

        # slow와 fast 포인터 초기화
        slow = fast = head
        curr = slow.next

        # 리스트 중간을 찾으면서 앞부분을 역순으로 변환
        while fast and fast.next:
            fast = fast.next.next  # fast는 두 칸씩 이동
            nxt = curr.next        # 다음 노드 저장
            curr.next = slow       # 현재 노드의 방향을 반대로 변경
            slow = curr            # slow를 한 칸 이동
            curr = nxt             # curr을 다음 노드로 이동

        # 리스트 길이가 홀수인지 확인하고 포인터 분리
        if fast:
            head1 = slow.next      # 중간 이후의 리스트 시작점
            head2 = curr          # 반대 방향 리스트 시작점
        else:
            head1 = slow.next
            head2 = slow
            head2.next = curr

        # 두 리스트를 비교하여 palindrome 여부 확인
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next

        return True

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 배열을 오름차순으로 정렬
        result = []  # 결과를 저장할 리스트

        for left in range(len(nums) - 2):  # 첫 번째 포인터 (left)를 설정
            # 이전 숫자와 동일하면 중복이므로 건너뛰기
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            target = -nums[left]  # 두 번째와 세 번째 숫자의 합이 이 값이 되어야 함
            mid, right = left + 1, len(nums) - 1  # 두 번째와 세 번째 포인터 초기화

            while mid < right:  # 두 번째 포인터(mid)와 세 번째 포인터(right) 간 탐색
                curr = nums[mid] + nums[right]  # 현재 두 숫자의 합 계산
                if target == curr:  # 세 숫자의 합이 0인 경우
                    result.append([nums[left], nums[mid], nums[right]])  # 결과에 추가
                    mid += 1  # 두 번째 포인터를 오른쪽으로 이동
                    right -= 1  # 세 번째 포인터를 왼쪽으로 이동

                    # 중복된 숫자를 건너뛰기
                    while mid <= right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid <= right and nums[right] == nums[right + 1]:
                        right -= 1
                elif target < curr:  # 현재 합이 목표보다 크면 세 번째 포인터 이동
                    right -= 1
                else:  # 현재 합이 목표보다 작으면 두 번째 포인터 이동
                    mid += 1

        return result  # 결과 반환

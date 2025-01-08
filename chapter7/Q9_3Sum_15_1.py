# Two Sum 문제 방법을 이용했는데 너무 느리다.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 배열을 오름차순으로 정렬
        result = set()  # 결과를 저장할 집합 (중복 제거)

        for left in range(len(nums) - 2):  # left 포인터: 첫 번째 숫자를 고정
            # 특정 숫자가 너무 많이 반복되면 건너뛰기
            if left + 4 < len(nums) - 2 and nums[left] == nums[left + 4]:
                continue

            complement = dict()  # 보완 값을 저장할 딕셔너리
            for mid in range(left + 1, len(nums)):  # mid 포인터: 두 번째 숫자를 고정
                if -nums[mid] in complement:  # 세 번째 숫자 확인
                    # 세 숫자의 합이 0이 되는 경우를 결과에 추가
                    result.add((complement[-nums[mid]][0], complement[-nums[mid]][1], nums[mid]))
                else:
                    # 현재 숫자 쌍 (nums[left], nums[mid])을 딕셔너리에 추가
                    complement[nums[left] + nums[mid]] = [nums[left], nums[mid]]

        # 결과를 리스트로 변환하여 반환
        return [list(x) for x in result]

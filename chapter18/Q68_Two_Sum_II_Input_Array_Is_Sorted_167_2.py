# My solutions2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            curr = numbers[left] + numbers[right]
            if curr > target:
                right -= 1
            elif curr < target:
                left += 1
            else:
                return [left + 1, right + 1]

        # 왜 처음에 투 포인터를 생각하지 못하고 이진 검색을 생각했을까?
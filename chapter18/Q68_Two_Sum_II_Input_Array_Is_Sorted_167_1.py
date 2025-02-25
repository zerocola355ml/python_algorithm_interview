# My solutions1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] > remainder:
                    right = mid - 1
                elif numbers[mid] < remainder:
                    left = mid + 1
                else:
                    return [i + 1, mid + 1]
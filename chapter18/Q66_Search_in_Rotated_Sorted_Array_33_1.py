# My solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: # 왼쪽이 제대로 정렬
                if nums[left] <= target <= nums[mid]: # 왼쪽을 탐색
                    right = mid - 1
                else: # 오른쪽을 탐색
                    left = mid + 1
            else: # 오른쪽이 제대로 정렬
                if nums[mid] <= target <= nums[right]: # 오른쪽을 탐색
                    left = mid + 1
                else: # 왼쪽을 탐색
                    right = mid - 1
        return -1
# My solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = right = 0
        curr = M = nums[0]

        while right < len(nums):
            if curr < 0:
                right += 1
                left = right
                if right < len(nums):
                    curr = nums[left]
            else:
                right += 1
                if right < len(nums):
                    curr += nums[right]
            M = max(M, curr)

        return M

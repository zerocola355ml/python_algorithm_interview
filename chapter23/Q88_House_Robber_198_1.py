# My solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        def helper(i):
            if i in memo:
                return memo[i]
            if len(nums) - i <= 2:
                memo[i] = max(nums[i:])
                return memo[i]
            memo[i] = max(nums[i] + helper(i + 2), helper(i + 1))
            return memo[i]
        return helper(0)
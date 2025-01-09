class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        while nums:
            nums.pop()
            result += nums.pop()
        return result
# Answer2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur_sum , max_sum = nums[0], nums[0]
        # nums = [-2, 1, -3, 4,-1,2,1,-5, 4]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num) # -2, 1, -2, 4, 3, 5, 6, 1, 5
            max_sum = max(max_sum, cur_sum)   # -2, 1,  1, 4, 4, 5, 6, 6, 6

        return max_sum
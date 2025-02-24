# My solutions3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_0, cnt_1, cnt_2 = 0, 0, 0
        for num in nums:
            if num == 0:
                cnt_0 += 1
            elif num == 1:
                cnt_1 += 1
            else:
                cnt_2 += 1
        nums[:] = [0] * cnt_0 + [1] * cnt_1 + [2] * cnt_2
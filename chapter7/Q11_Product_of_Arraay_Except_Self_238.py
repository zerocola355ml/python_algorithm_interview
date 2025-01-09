class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        multiple = 1
        for left in range(len(nums)):
            result.append(multiple)
            multiple *= nums[left]

        multiple = 1

        for right in range(len(nums) - 1, 0, -1):
            multiple *= nums[right]
            result[right - 1] *= multiple

        return result
# My solution2
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            helper(index + 1, path)
            path.append(nums[index])
            helper(index + 1, path)
            path.pop()

        helper(0, [])
        return result
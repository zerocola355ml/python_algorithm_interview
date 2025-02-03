# My solution2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    helper(path)
                    path.pop()

        helper([])

        return result

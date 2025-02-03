# My solution3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(path, idx):
            result.append(path[:])  # 습관적으로 종료 조건을 idx == len(nums)로 해서 못풀었음.
            for i in range(idx, len(nums)):
                path.append(nums[i])
                helper(path, i + 1)
                path.pop()

        helper([], 0)

        return result
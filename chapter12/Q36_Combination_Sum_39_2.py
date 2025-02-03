# My solution2
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(path, curr, start):
            if curr > target:
                return
            if curr == target:
                result.append(path[:])
                return
            for idx in range(start, len(candidates)):
                path.append(candidates[idx])
                helper(path, curr + candidates[idx], idx)
                path.pop()

        helper([], 0, 0)

        return result
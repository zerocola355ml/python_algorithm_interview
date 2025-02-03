# Answer
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
                helper(path + [candidates[idx]], curr + candidates[idx], idx)

        helper([], 0, 0)

        return result
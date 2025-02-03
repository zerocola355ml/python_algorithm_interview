# My solution1
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(curr, path, index):
            if curr == target:
                result.append(path[:])
                return
            if curr < target:
                for i in range(index, len(candidates)):
                    path.append(candidates[i])
                    helper(curr + candidates[i], path, i)
                    path.pop()
            return

        helper(0, [], 0)

        return result
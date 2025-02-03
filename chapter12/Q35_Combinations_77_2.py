# My solution2
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(path, num):
            if len(path) == k:
                result.append(path[:])
                return
            if num <= n:
                helper(path, num + 1)
                path.append(num)
                helper(path, num + 1)
                path.pop()

        result = []
        helper([], 1)
        return result
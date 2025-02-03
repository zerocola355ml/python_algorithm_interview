# My solution3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(path, start):
            if len(path) == k:
                result.append(path[:])
                return
            for num in range(start, n + 1):
                path.append(num)
                helper(path, num + 1)
                path.pop()

        result = []
        helper([], 1)
        return result
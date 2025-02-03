# My solution4
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def helper(start, k, path):
            if k == 0:
                result.append(path[:])
                return
            for num in range(start, n + 2 - k):
                path.append(num)
                helper(num + 1, k - 1, path)
                path.pop()

        helper(1, k, [])

        return result
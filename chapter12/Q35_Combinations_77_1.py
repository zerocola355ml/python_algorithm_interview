# My solution1
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(path, n, k):
            if len(path) == k:
                result.append(path)
                return
            for num in range(1, n + 1):
                if not path or path[-1] < num:
                    helper(path + [num], n , k)

        result = []
        helper([], n, k)
        return result
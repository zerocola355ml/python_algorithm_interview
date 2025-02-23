# My solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        intervals.reverse()
        while intervals:
            a, b = intervals.pop()
            while intervals and intervals[-1][0] <= b:
                c, d = intervals.pop()
                a, b = min(a, c), max(b, d)
            result.append([a, b])

        return result
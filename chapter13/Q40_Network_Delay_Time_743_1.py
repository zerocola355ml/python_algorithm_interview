# My solution
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        result = [float("inf")] * n
        result[k - 1] = 0

        for a, b, c in times:
            graph[a].append((b, c))

        left = set(graph)
        search = k

        if k not in left:
            return -1

        while left:
            for neighbor in graph[search]:
                result[neighbor[0] - 1] = min(result[neighbor[0] - 1], result[search - 1] + neighbor[1])
            left.remove(search)
            if left:
                search = min(left, key=lambda x: result[x - 1])

        result = max(result)
        if result == float("inf"):
            return -1
        else:
            return result
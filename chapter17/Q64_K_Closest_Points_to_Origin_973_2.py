# Answer
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heapq.heappush(heap, (x ** 2 + y ** 2, x, y))

        result = []

        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result
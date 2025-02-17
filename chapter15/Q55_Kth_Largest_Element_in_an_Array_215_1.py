# My solution1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, (-num, num))
        for _ in range(k - 1):
            heapq.heappop(heap)
        return heapq.heappop(heap)[1]
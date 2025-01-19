# Answer1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = []
        result = []

        for num in freq:
            heapq.heappush(heap, (-freq[num], num))

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
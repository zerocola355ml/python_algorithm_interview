# My solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        return [x for (x, y) in count.most_common(k)]